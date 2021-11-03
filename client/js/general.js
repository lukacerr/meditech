AOS.init();

// jPost
$.extend({
  jpost: function (url, body) {
    return $.ajax({
      type: 'POST',
      url: 'http://localhost:8000/' + url,
      data: JSON.stringify(body),
      contentType: 'application/json',
      dataType: 'json',
    });
  },
});

async function CheckLogin(data, noRedirect) {
  const post = data ?? GetSessionLogin();

  return await $.jpost('login', post).then((res) => {
    if (res == true) {
      SaveSessionLogin(post);
      return true;
    }

    if (!noRedirect) GoToIndex();
    return res;
  });
}

function SaveSessionLogin(data) {
  sessionStorage.setItem('meditech-login', JSON.stringify(data));
}

function DeleteSessionLogin() {
  sessionStorage.removeItem('meditech-login');
}

function GetSessionLogin() {
  return JSON.parse(sessionStorage.getItem('meditech-login'));
}

function GoToIndex() {
  location.href = './index.html';
}

$('#GoMenu').click(() => {
  location.href = './menu.html';
});
