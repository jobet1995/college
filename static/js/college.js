/**
 * ============================================================================
 * COLLEGE - GLOBAL JAVASCRIPT
 * ============================================================================
 * This file contains global JavaScript utilities, AJAX handlers, and helpers.
 * NO component-specific code should be added here.
 * 
 * Dependencies: jQuery, SweetAlert2
 * ============================================================================
 */

(function ($) {
  'use strict';

  /**
   * ============================================================================
   * MAIN COLLEGE APPLICATION CLASS (OOP)
   * ============================================================================
   */
  class CollegeApp {
    constructor() {
      this.config = {
        ajaxTimeout: 30000, // 30 seconds
        animationDuration: 300,
        scrollOffset: 80,
        debounceDelay: 300
      };

      this.state = {
        isLoading: false,
        isMobile: window.innerWidth < 768,
        currentScrollPosition: 0,
        previousScrollPosition: 0
      };

      this.init();
    }

    /**
     * Initialize the application
     */
    init() {
      console.log('College App Initializing...');
      
      // Bind event listeners
      this.bindEvents();
      
      // Initialize utilities
      this.initSmoothScroll();
      this.initScrollDetection();
      this.initResponsiveHandlers();
      
      console.log('College App Initialized ✓');
    }

    /**
     * Bind global event listeners
     */
    bindEvents() {
      const self = this;

      // Window resize handler (debounced)
      $(window).on('resize', this.debounce(function () {
        self.handleResize();
      }, this.config.debounceDelay));

      // Window scroll handler (throttled)
      $(window).on('scroll', this.throttle(function () {
        self.handleScroll();
      }, 100));

      // Handle all form submissions with AJAX class
      $(document).on('submit', 'form.ajax-form', function (e) {
        e.preventDefault();
        self.handleAjaxFormSubmit($(this));
      });

      // Handle external links
      $(document).on('click', 'a[target="_blank"]', function () {
        console.log('External link clicked:', $(this).attr('href'));
      });
    }

    /**
     * ========================================================================
     * AJAX UTILITIES
     * ========================================================================
     */

    /**
     * Generic AJAX GET request
     * @param {string} url - The URL to send the request to
     * @param {object} data - Data to send with the request
     * @param {object} options - Additional options
     * @returns {Promise}
     */
    ajaxGet(url, data = {}, options = {}) {
      const defaults = {
        showLoader: true,
        showSuccessMessage: false,
        successMessage: 'Data loaded successfully',
        errorMessage: 'Failed to load data'
      };

      const settings = $.extend({}, defaults, options);

      if (settings.showLoader) {
        this.showLoader();
      }

      return $.ajax({
        url: url,
        type: 'GET',
        data: data,
        dataType: 'json',
        timeout: this.config.ajaxTimeout,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
        .done((response) => {
          this.handleAjaxSuccess(response, settings);
        })
        .fail((xhr, status, error) => {
          this.handleAjaxError(xhr, status, error, settings);
        })
        .always(() => {
          if (settings.showLoader) {
            this.hideLoader();
          }
        });
    }

    /**
     * Generic AJAX POST request
     * @param {string} url - The URL to send the request to
     * @param {object} data - Data to send with the request
     * @param {object} options - Additional options
     * @returns {Promise}
     */
    ajaxPost(url, data = {}, options = {}) {
      const defaults = {
        showLoader: true,
        showSuccessMessage: true,
        successMessage: 'Operation completed successfully',
        errorMessage: 'Operation failed',
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8'
      };

      const settings = $.extend({}, defaults, options);

      if (settings.showLoader) {
        this.showLoader();
      }

      // Get CSRF token for Django
      const csrfToken = this.getCSRFToken();

      return $.ajax({
        url: url,
        type: 'POST',
        data: data,
        dataType: 'json',
        timeout: this.config.ajaxTimeout,
        contentType: settings.contentType,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrfToken
        }
      })
        .done((response) => {
          this.handleAjaxSuccess(response, settings);
        })
        .fail((xhr, status, error) => {
          this.handleAjaxError(xhr, status, error, settings);
        })
        .always(() => {
          if (settings.showLoader) {
            this.hideLoader();
          }
        });
    }

    /**
     * AJAX form submission handler
     * @param {jQuery} $form - The form element
     */
    handleAjaxFormSubmit($form) {
      const url = $form.attr('action') || window.location.href;
      const method = ($form.attr('method') || 'POST').toUpperCase();
      const formData = $form.serialize();

      const options = {
        showLoader: true,
        showSuccessMessage: true,
        successMessage: $form.data('success-message') || 'Form submitted successfully',
        errorMessage: $form.data('error-message') || 'Form submission failed'
      };

      if (method === 'GET') {
        this.ajaxGet(url, formData, options);
      } else {
        this.ajaxPost(url, formData, options);
      }
    }

    /**
     * Handle successful AJAX response
     * @param {object} response - The JSON response from server
     * @param {object} settings - Settings object
     */
    handleAjaxSuccess(response, settings) {
      console.log('AJAX Success:', response);

      // Check if response has a success property
      if (response.success === false) {
        this.showError(response.message || settings.errorMessage);
        return;
      }

      // Show success message if configured
      if (settings.showSuccessMessage) {
        this.showSuccess(response.message || settings.successMessage);
      }

      // Trigger custom event for success
      $(document).trigger('ajax:success', [response]);
    }

    /**
     * Handle AJAX error
     * @param {object} xhr - XMLHttpRequest object
     * @param {string} status - Status text
     * @param {string} error - Error message
     * @param {object} settings - Settings object
     */
    handleAjaxError(xhr, status, error, settings) {
      console.error('AJAX Error:', { xhr, status, error });

      let errorMessage = settings.errorMessage;

      // Try to parse JSON error response
      if (xhr.responseJSON && xhr.responseJSON.message) {
        errorMessage = xhr.responseJSON.message;
      } else if (xhr.responseText) {
        try {
          const response = JSON.parse(xhr.responseText);
          errorMessage = response.message || errorMessage;
        } catch (e) {
          // Not JSON, use default message
        }
      }

      // Handle specific HTTP status codes
      switch (xhr.status) {
        case 400:
          errorMessage = 'Bad request. Please check your input.';
          break;
        case 401:
          errorMessage = 'Unauthorized. Please login again.';
          break;
        case 403:
          errorMessage = 'Access forbidden.';
          break;
        case 404:
          errorMessage = 'Resource not found.';
          break;
        case 500:
          errorMessage = 'Server error. Please try again later.';
          break;
        case 0:
          if (status === 'timeout') {
            errorMessage = 'Request timeout. Please try again.';
          } else if (status === 'abort') {
            errorMessage = 'Request aborted.';
          }
          break;
      }

      this.showError(errorMessage);

      // Trigger custom event for error
      $(document).trigger('ajax:error', [xhr, status, error]);
    }

    /**
     * Get CSRF token from cookies (for Django)
     * @returns {string} CSRF token
     */
    getCSRFToken() {
      const name = 'csrftoken';
      let cookieValue = null;

      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }

      return cookieValue || '';
    }

    /**
     * ========================================================================
     * SWEETALERT UTILITIES
     * ========================================================================
     */

    /**
     * Show success message
     * @param {string} message - Success message
     * @param {string} title - Optional title
     * @param {object} options - Additional SweetAlert options
     */
    showSuccess(message, title = 'Success', options = {}) {
      const defaults = {
        icon: 'success',
        title: title,
        text: message,
        toast: false,
        position: 'center',
        showConfirmButton: true,
        timer: 3000,
        timerProgressBar: true
      };

      const settings = $.extend({}, defaults, options);
      Swal.fire(settings);
    }

    /**
     * Show error message
     * @param {string} message - Error message
     * @param {string} title - Optional title
     * @param {object} options - Additional SweetAlert options
     */
    showError(message, title = 'Error', options = {}) {
      const defaults = {
        icon: 'error',
        title: title,
        text: message,
        toast: false,
        position: 'center',
        showConfirmButton: true,
        confirmButtonText: 'OK'
      };

      const settings = $.extend({}, defaults, options);
      Swal.fire(settings);
    }

    /**
     * Show warning message
     * @param {string} message - Warning message
     * @param {string} title - Optional title
     * @param {object} options - Additional SweetAlert options
     */
    showWarning(message, title = 'Warning', options = {}) {
      const defaults = {
        icon: 'warning',
        title: title,
        text: message,
        toast: false,
        position: 'center',
        showConfirmButton: true
      };

      const settings = $.extend({}, defaults, options);
      Swal.fire(settings);
    }

    /**
     * Show info message
     * @param {string} message - Info message
     * @param {string} title - Optional title
     * @param {object} options - Additional SweetAlert options
     */
    showInfo(message, title = 'Information', options = {}) {
      const defaults = {
        icon: 'info',
        title: title,
        text: message,
        toast: false,
        position: 'center',
        showConfirmButton: true
      };

      const settings = $.extend({}, defaults, options);
      Swal.fire(settings);
    }

    /**
     * Show confirmation dialog
     * @param {string} message - Confirmation message
     * @param {string} title - Optional title
     * @param {function} onConfirm - Callback function on confirm
     * @param {object} options - Additional SweetAlert options
     */
    showConfirm(message, title = 'Are you sure?', onConfirm, options = {}) {
      const defaults = {
        icon: 'question',
        title: title,
        text: message,
        showCancelButton: true,
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        confirmButtonColor: '#3b82f6',
        cancelButtonColor: '#ef4444',
        reverseButtons: true
      };

      const settings = $.extend({}, defaults, options);

      Swal.fire(settings).then((result) => {
        if (result.isConfirmed && typeof onConfirm === 'function') {
          onConfirm();
        }
      });
    }

    /**
     * Show toast notification (top-right corner)
     * @param {string} message - Toast message
     * @param {string} icon - Icon type (success, error, warning, info)
     */
    showToast(message, icon = 'success') {
      const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer);
          toast.addEventListener('mouseleave', Swal.resumeTimer);
        }
      });

      Toast.fire({
        icon: icon,
        title: message
      });
    }

    /**
     * Show loading/processing alert
     * @param {string} message - Loading message
     */
    showLoader(message = 'Processing...') {
      Swal.fire({
        title: message,
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        willOpen: () => {
          Swal.showLoading();
        }
      });

      this.state.isLoading = true;
    }

    /**
     * Hide loader
     */
    hideLoader() {
      if (this.state.isLoading) {
        Swal.close();
        this.state.isLoading = false;
      }
    }

    /**
     * ========================================================================
     * UTILITY FUNCTIONS
     * ========================================================================
     */

    /**
     * Smooth scroll to element or position
     * @param {string|number} target - Selector or scroll position
     * @param {number} offset - Offset from target
     * @param {number} duration - Animation duration
     */
    scrollTo(target, offset = 0, duration = 800) {
      let scrollPosition;

      if (typeof target === 'number') {
        scrollPosition = target;
      } else {
        const $target = $(target);
        if ($target.length === 0) return;
        scrollPosition = $target.offset().top - offset;
      }

      $('html, body').animate({
        scrollTop: scrollPosition
      }, duration);
    }

    /**
     * Initialize smooth scroll for anchor links
     */
    initSmoothScroll() {
      const self = this;

      $(document).on('click', 'a[href^="#"]:not([href="#"])', function (e) {
        const target = $(this).attr('href');

        if ($(target).length > 0) {
          e.preventDefault();
          self.scrollTo(target, self.config.scrollOffset);

          // Update URL without jumping
          if (history.pushState) {
            history.pushState(null, null, target);
          }
        }
      });
    }

    /**
     * Initialize scroll detection
     */
    initScrollDetection() {
      const self = this;

      $(window).on('scroll', function () {
        const scrollTop = $(this).scrollTop();

        // Update state
        self.state.previousScrollPosition = self.state.currentScrollPosition;
        self.state.currentScrollPosition = scrollTop;

        // Add/remove scroll class to body
        if (scrollTop > 100) {
          $('body').addClass('scrolled');
        } else {
          $('body').removeClass('scrolled');
        }

        // Detect scroll direction
        if (scrollTop > self.state.previousScrollPosition) {
          $('body').addClass('scroll-down').removeClass('scroll-up');
        } else {
          $('body').addClass('scroll-up').removeClass('scroll-down');
        }
      });
    }

    /**
     * Initialize responsive handlers
     */
    initResponsiveHandlers() {
      this.updateResponsiveState();
    }

    /**
     * Handle window resize
     */
    handleResize() {
      this.updateResponsiveState();
      console.log('Window resized - isMobile:', this.state.isMobile);

      // Trigger custom event
      $(document).trigger('app:resize', [this.state.isMobile]);
    }

    /**
     * Handle window scroll
     */
    handleScroll() {
      // Custom scroll handling can be added here
      $(document).trigger('app:scroll', [this.state.currentScrollPosition]);
    }

    /**
     * Update responsive state
     */
    updateResponsiveState() {
      const width = window.innerWidth;
      this.state.isMobile = width < 768;
      this.state.isTablet = width >= 768 && width < 1024;
      this.state.isDesktop = width >= 1024;

      // Update body classes
      $('body')
        .toggleClass('is-mobile', this.state.isMobile)
        .toggleClass('is-tablet', this.state.isTablet)
        .toggleClass('is-desktop', this.state.isDesktop);
    }

    /**
     * Debounce function
     * @param {function} func - Function to debounce
     * @param {number} wait - Wait time in milliseconds
     * @returns {function}
     */
    debounce(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    }

    /**
     * Throttle function
     * @param {function} func - Function to throttle
     * @param {number} limit - Time limit in milliseconds
     * @returns {function}
     */
    throttle(func, limit) {
      let inThrottle;
      return function executedFunction(...args) {
        if (!inThrottle) {
          func.apply(this, args);
          inThrottle = true;
          setTimeout(() => inThrottle = false, limit);
        }
      };
    }

    /**
     * Parse JSON safely
     * @param {string} jsonString - JSON string to parse
     * @param {*} defaultValue - Default value if parsing fails
     * @returns {*}
     */
    parseJSON(jsonString, defaultValue = null) {
      try {
        return JSON.parse(jsonString);
      } catch (e) {
        console.error('JSON Parse Error:', e);
        return defaultValue;
      }
    }

    /**
     * Format number with commas
     * @param {number} num - Number to format
     * @returns {string}
     */
    formatNumber(num) {
      return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }

    /**
     * Truncate text
     * @param {string} text - Text to truncate
     * @param {number} length - Maximum length
     * @param {string} suffix - Suffix to add
     * @returns {string}
     */
    truncateText(text, length = 100, suffix = '...') {
      if (text.length <= length) return text;
      return text.substring(0, length).trim() + suffix;
    }

    /**
     * Copy text to clipboard
     * @param {string} text - Text to copy
     */
    copyToClipboard(text) {
      const self = this;

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text)
          .then(() => {
            self.showToast('Copied to clipboard!', 'success');
          })
          .catch((err) => {
            console.error('Clipboard Error:', err);
            self.showError('Failed to copy to clipboard');
          });
      } else {
        // Fallback for older browsers
        const $temp = $('<textarea>');
        $('body').append($temp);
        $temp.val(text).select();
        document.execCommand('copy');
        $temp.remove();
        self.showToast('Copied to clipboard!', 'success');
      }
    }

    /**
     * Validate email
     * @param {string} email - Email to validate
     * @returns {boolean}
     */
    isValidEmail(email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    }

    /**
     * Validate URL
     * @param {string} url - URL to validate
     * @returns {boolean}
     */
    isValidUrl(url) {
      try {
        new URL(url);
        return true;
      } catch (e) {
        return false;
      }
    }
  }

  /**
   * ============================================================================
   * INITIALIZE APPLICATION ON DOCUMENT READY
   * ============================================================================
   */
  $(document).ready(function () {
    // Create global instance
    window.CollegeApp = new CollegeApp();

    // Make it accessible via window object for external scripts
    window.App = window.CollegeApp;

    console.log('College App Ready! 🎓');
  });

})(jQuery);
