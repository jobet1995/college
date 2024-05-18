function fetchData(url, objData) {
    var results = null;
    if (objData === 'undefined' || objData === null) objData = null;
    $.ajax({
        url: url,
        async: false,
        type: "POST",
        dataType: "JSON",
        data: objData,
        success: function(response) {
            results = response;
        }
    });
    return results;
}

function insertData(url, objData) {
    var results = null;
    $.ajax({
        url: url,
        async: false,
        type: "POST",
        dataType: "JSON",
        data: objData,
        success: function(response) {
            results = response;
        }
    });
    return results;
}

function deleteData(url, objData) {
    return insertData(url, objData);
}

function updateData(url, objData) {
    return insertData(url, objData);
}