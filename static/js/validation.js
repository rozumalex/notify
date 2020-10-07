$(document).ready(function() {
  $('form[id="signup-form"]').validate({
    rules: {
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,
        minlength: 10,
      }
    },
    messages: {
      email: {
        required: 'Email required',
        email: 'Enter a valid email adress'
      },
      password: {
        required: 'Password required',
        minlength: 'Password must be atleast 10 characters long'
      }
    },
    submitHandler: function(form) {
      form.submit();
    }
  });
});


$(document).ready(function() {
  $('form[id="login-form"]').validate({
    rules: {
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true
      }
    },
    messages: {
      email: {
        required: 'Email required',
        email: 'Enter a valid email adress'
      },
      password: {
        required: 'Password required'
      }
    },
    submitHandler: function(form) {
      form.submit();
    }
  });
});
