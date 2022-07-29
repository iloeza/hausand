$(document).on("click", ".open-AddBookDialog", function () {
    let myBookId = $(this).data('id');
    let myBookName = $(this).data('name');
    console.log($(this).data('name'))
    $(".modal-body #bookId").val(myBookId);
    $(".modal-header #books__modalLabel").html(`Donar libro: ${myBookName}`);
});
