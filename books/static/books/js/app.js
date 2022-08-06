$(document).on("click", ".open-AddBookDialog", function () {
    let myBookId = $(this).data('id');
    let myBookName = $(this).data('name');
    $(".modal-body #bookId").val(myBookId);
    $(".modal-header #books__modalLabel").html(`Donar libro: ${myBookName}`);
});

$(document).ready(function () {
    setTimeout(() => {
        if ($("#success-msg").length > 0) {
            $("#success-msg").remove()
        }
    }, 3000)
});