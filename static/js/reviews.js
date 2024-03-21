

function detail_display(display_mode, r_id) {

    if (r_id) {
        review_id = r_id;
    } else {
        review_id = $(this).data("id");
    }
    let detailBaseUrl = $("#detail-base-url").data("url");
    var url = `${detailBaseUrl}?id=${review_id}`
    if (display_mode === "edit") {
        url += "&mode=edit";
    }
    console.log(review_id);

    // fetch details from server
    $.ajax({
        url: url,
        dataType: 'json',
        timeout: 1000,   // in msec
        success: function (data) {
            $("#reviewDetail").html(data.content);
        },
        complete: function (textStatus) {
            if (textStatus === 'error' || textStatus === 'timeout') {
                alert("Server Error. Try later.");
            }
        }
    })
}

function reviewEdit(review_id) {
    detail_display("edit", review_id);
}

function reviewEditSubmit() {
    let review_id = $(this).data("id");
    let detailBaseUrl = $("#detail-base-url").data("url");
    var url = `${detailBaseUrl}?id=${review_id}`;

    $.ajax({
        url: url,
        method: "post",
        dataType: "json",
        timeout: 1_000,
        data: {
            id: review_id,
            blurb: $("#reviewEditBlurb").val(),
            review: $("#reviewEditReview").val()
        },
        success: function() {
            alert("Review updated successfully.");
            // reload dt table
            let is_checked = $("#searchSelf").is(":checked");
            reloadDT(is_checked);
        },
        error: function(errorThrown) {
            alert("something wrong!!!");
        },
        complete: function(textStatus) {
            if (textStatus === 'error' || textStatus === 'timeout') {
                alert("Server Error. Try later.");
            }
            detail_display("view", review_id);
        }
    });

    return false;
}

function reviewEditCancel() {
    let review_id = $(this).data("id");
    detail_display("view", review_id);
    return false;
}


function reviewAdd() {
    $.ajax({
        url: "/reviews/add/",
        method: "get",
        dataType: "json",
        timeout: 1_000,
        success: function(data) {
            $("#reviewDetail").html(data.content);
        },
        complete: function(textStatus) {
            if (textStatus === 'error' || textStatus === 'timeout') {
                alert("Server Error. Try later.");
            }
        }
    });
}


function reviewAddCancel() {
    $("#reviewDetail").html("Select a review from the Summary List");
    return false;
}