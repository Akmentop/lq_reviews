

function detail_display() {

    review_id = $(this).data("id");
    console.log(review_id);

    // fetch details from server
    let detailBaseUrl = $("#detail-base-url").data("url");
    $.ajax({
        url: `${detailBaseUrl}?id=${review_id}`,
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
    alert(review_id);

    // pup up modal
    // $("#reviewEditModal").modal("show");

}

