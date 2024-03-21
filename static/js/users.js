

function loginUser(username, password) {
    let login_url = $("#login-url").data("url");
    $.ajax({
        type: 'POST',
        url: "/accounts/login/",
        data:  { username: username, password: password },
        dataType: "json",
        success: function (data) {
            console.log("Login success!");
            window.location.replace("/");
        },
        error: function (errorThrown) {
            console.log(errorThrown.responseJSON.message);
            alert(errorThrown.responseJSON.message + '. Signup failed.' );
        },
        complete: function() {
            // close and clean up form
            $("#SignupModal").modal("hide");
            username.val("");
            password.val("");
        },
    });
}

function reloadDT(is_checked) {

    let url=$("#searchTable-url").data("url") + "?self=" + is_checked;
    console.log(url);
    searchResultTable.ajax.url(url);
    searchResultTable.ajax.reload();
}

function init() {

    $("#loginPopup").click(function () {
        $("#loginUsername").val('');
        $("#loginPwd").val('');
        $("#LoginModal").modal("show");
    });

    $("#signup").click(function () {
        $("#SignupModal").modal("show");
    });


    // search self checkbox
    $(document).on("click", "#searchSelf", function () {

        let is_checked = $(this).is(":checked");
        reloadDT(is_checked);

    });

    $(document).on("click", "#loginButton", function() {
        let username = $("#loginUsername").val();
        let password = $("#loginPwd").val();
        loginUser(username, password);
    });

    // signup button click
    $("#signupButton").click(function () {
        let input_username =  $("#su_username");
        let username = input_username.val();

        if (username.length < 4 || /\s/.test(username)) {
            alert("username must be 4 chars or longer, no space in it.");
        }

        let input_pwd_1 = $("#su_pwd_1");
        let input_pwd_2 = $("#su_pwd_2");
        let pwd_1 =  input_pwd_1.val();
        let pwd_2 =  input_pwd_2.val();
        if   (pwd_1.length < 4) {
            alert("Password must be 4 chars or longer!");
        } else if (pwd_1 !== pwd_2) {
            alert("Passwords do not match!");
        }

        // submit it!
        let signup_url = $("#signup-url").data("url");
        $.ajax({
            type: 'POST',
            url: signup_url,
            data: { username: username, password: pwd_1 },
            dataType: 'json',
            success: function (data) {
                alert("Welcome to our Member Area!");
                loginUser(username, pwd_1);
            },
            error: function (errorThrown) {
                console.log(errorThrown.responseJSON.message);
                alert(errorThrown.responseJSON.message + '. Signup failed.' );
            },
            complete: function() {
                // close and clean up form
                $("#SignupModal").modal("hide");
                input_username.val("");
                input_pwd_1.val("");
                input_pwd_2.val("");
            }
        });
    });
}

$(function() {
    init();
})