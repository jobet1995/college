/**
 * ============================================================================
 * NAVBAR MODULE - OOP Implementation with jQuery and AJAX
 * ============================================================================
 * Handles navbar interactions, mobile menu toggle, and dynamic content loading
 */

class NavbarManager {
    /**
     * Initialize the Navbar Manager
     * @param {Object} options - Configuration options
     */
    constructor(options = {}) {
        this.config = {
            burgerSelector: '.navbar-burger',
            menuSelector: '.navbar-menu',
            itemSelector: '.navbar-item',
            activeClass: 'is-active',
            animationDuration: 300,
            ajaxEndpoint: options.ajaxEndpoint || '/api/navbar/',
            ...options
        };

        this.state = {
            isMenuOpen: false,
            activeItem: null,
            menuData: null
        };

        this.init();
    }

    /**
     * Initialize the navbar functionality
     */
    init() {
        this.cacheElements();
        this.bindEvents();
        this.loadMenuData();
        this.setActiveMenuItem();
    }

    /**
     * Cache jQuery elements for better performance
     */
    cacheElements() {
        this.$burger = $(this.config.burgerSelector);
        this.$menu = $(this.config.menuSelector);
        this.$menuItems = $(this.config.itemSelector);
        this.$body = $('body');
    }

    /**
     * Bind event listeners
     */
    bindEvents() {
        // Mobile menu toggle
        this.$burger.on('click', (e) => this.handleBurgerClick(e));

        // Menu item clicks
        this.$menuItems.on('click', (e) => this.handleMenuItemClick(e));

        // Close menu on outside click
        $(document).on('click', (e) => this.handleOutsideClick(e));

        // Close menu on escape key
        $(document).on('keydown', (e) => this.handleEscapeKey(e));

        // Handle window resize
        $(window).on('resize', () => this.handleResize());
    }

    /**
     * Handle burger icon click
     * @param {Event} e - Click event
     */
    handleBurgerClick(e) {
        e.preventDefault();
        e.stopPropagation();
        this.toggleMenu();
    }

    /**
     * Toggle mobile menu open/close
     */
    toggleMenu() {
        this.state.isMenuOpen = !this.state.isMenuOpen;

        this.$burger.toggleClass(this.config.activeClass);
        this.$menu.toggleClass(this.config.activeClass);

        // Update ARIA attributes for accessibility
        this.$burger.attr('aria-expanded', this.state.isMenuOpen);

        // Prevent body scroll when menu is open
        if (this.state.isMenuOpen) {
            this.$body.css('overflow', 'hidden');
        } else {
            this.$body.css('overflow', '');
        }

        // Trigger custom event
        $(document).trigger('navbar:toggle', { isOpen: this.state.isMenuOpen });
    }

    /**
     * Close the mobile menu
     */
    closeMenu() {
        if (this.state.isMenuOpen) {
            this.toggleMenu();
        }
    }

    /**
     * Handle menu item click
     * @param {Event} e - Click event
     */
    handleMenuItemClick(e) {
        const $item = $(e.currentTarget);
        const href = $item.attr('href');

        // Remove active class from all items
        this.$menuItems.removeClass(this.config.activeClass);

        // Add active class to clicked item
        $item.addClass(this.config.activeClass);

        // Store active item
        this.state.activeItem = href;

        // Close mobile menu after selection
        if (window.innerWidth < 1024) {
            setTimeout(() => this.closeMenu(), 200);
        }

        // Track navigation event via AJAX
        this.trackNavigation(href);
    }

    /**
     * Handle clicks outside the menu
     * @param {Event} e - Click event
     */
    handleOutsideClick(e) {
        if (this.state.isMenuOpen) {
            const $target = $(e.target);
            if (!$target.closest(this.config.menuSelector).length && 
                !$target.closest(this.config.burgerSelector).length) {
                this.closeMenu();
            }
        }
    }

    /**
     * Handle escape key press
     * @param {Event} e - Keydown event
     */
    handleEscapeKey(e) {
        if (e.key === 'Escape' && this.state.isMenuOpen) {
            this.closeMenu();
        }
    }

    /**
     * Handle window resize
     */
    handleResize() {
        // Close menu on desktop resize
        if (window.innerWidth >= 1024 && this.state.isMenuOpen) {
            this.closeMenu();
        }
    }

    /**
     * Set active menu item based on current URL
     */
    setActiveMenuItem() {
        const currentPath = window.location.pathname;

        this.$menuItems.each((index, item) => {
            const $item = $(item);
            const href = $item.attr('href');

            if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
                $item.addClass(this.config.activeClass);
                this.state.activeItem = href;
            }
        });
    }

    /**
     * Load menu data via AJAX
     * @returns {Promise} AJAX promise
     */
    loadMenuData() {
        return $.ajax({
            url: this.config.ajaxEndpoint,
            method: 'GET',
            dataType: 'json',
            success: (response) => this.handleMenuDataSuccess(response),
            error: (xhr, status, error) => this.handleMenuDataError(xhr, status, error)
        });
    }

    /**
     * Handle successful menu data load
     * @param {Object} response - JSON response from server
     */
    handleMenuDataSuccess(response) {
        if (response.success && response.data) {
            this.state.menuData = response.data;
            console.log('Navbar: Menu data loaded successfully', response.data);

            // Trigger custom event
            $(document).trigger('navbar:dataLoaded', { data: response.data });

            // Optionally update menu items dynamically
            if (response.data.items) {
                this.updateMenuItems(response.data.items);
            }
        }
    }

    /**
     * Handle menu data load error
     * @param {Object} xhr - XMLHttpRequest object
     * @param {String} status - Error status
     * @param {String} error - Error message
     */
    handleMenuDataError(xhr, status, error) {
        console.warn('Navbar: Failed to load menu data', {
            status: status,
            error: error,
            response: xhr.responseJSON
        });

        // Use fallback menu data
        this.state.menuData = this.getFallbackMenuData();
    }

    /**
     * Update menu items dynamically
     * @param {Array} items - Array of menu item objects
     */
    updateMenuItems(items) {
        // This method can be used to dynamically update menu items
        // based on user permissions, features, etc.
        console.log('Navbar: Updating menu items', items);
    }

    /**
     * Track navigation event via AJAX
     * @param {String} href - Navigation URL
     */
    trackNavigation(href) {
        $.ajax({
            url: '/api/analytics/track/',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                event: 'navbar_click',
                url: href,
                timestamp: new Date().toISOString()
            }),
            contentType: 'application/json',
            success: (response) => {
                if (response.success) {
                    console.log('Navbar: Navigation tracked', href);
                }
            },
            error: (xhr, status, error) => {
                console.warn('Navbar: Failed to track navigation', error);
            }
        });
    }

    /**
     * Get fallback menu data
     * @returns {Object} Fallback menu configuration
     */
    getFallbackMenuData() {
        return {
            items: [
                { label: 'Home', url: '/', icon: 'home' },
                { label: 'About', url: '/about/', icon: 'info' },
                { label: 'Academics', url: '/academics/', icon: 'book' },
                { label: 'Admissions', url: '/admissions/', icon: 'user-plus' },
                { label: 'Campus Life', url: '/campus-life/', icon: 'users' },
                { label: 'Events', url: '/events/', icon: 'calendar' },
                { label: 'News', url: '/news/', icon: 'newspaper' },
                { label: 'Faculty & Staff', url: '/faculty-staff/', icon: 'briefcase' },
                { label: 'Research', url: '/research/', icon: 'flask' },
                { label: 'Contact', url: '/contact/', icon: 'envelope' }
            ]
        };
    }

    /**
     * Get current menu state
     * @returns {Object} Current state
     */
    getState() {
        return { ...this.state };
    }

    /**
     * Destroy the navbar instance
     */
    destroy() {
        this.$burger.off('click');
        this.$menuItems.off('click');
        $(document).off('click keydown');
        $(window).off('resize');
        this.$body.css('overflow', '');
    }
}

// ============================================================================
// Initialize on DOM Ready
// ============================================================================
$(document).ready(function() {
    // Initialize navbar manager
    window.navbarManager = new NavbarManager({
        ajaxEndpoint: '/api/navbar/',
        animationDuration: 300
    });

    // Example: Listen to custom events
    $(document).on('navbar:toggle', function(e, data) {
        console.log('Navbar menu toggled:', data.isOpen ? 'Open' : 'Closed');
    });

    $(document).on('navbar:dataLoaded', function(e, data) {
        console.log('Navbar data loaded:', data);
    });
});
