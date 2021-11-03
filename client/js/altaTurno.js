let session = GetSessionLogin() ?? null;
if (!session) GoToIndex();

CheckLogin(session).then((x) => {
  if (x == true) {
    // TODO:
  } else GoToIndex();
});

const errMsg = $('#errMessage');
const sucMsg = $('#sucMessage');

$('#btnSearch').click(() => {
  session.id = $('#inputId')[0]?.value;
  if (session.id) {
    errMsg.fadeOut(100);
    sucMsg.fadeOut(100);

    $.jpost('altaTurno', session).then((res) => {
      if (res == 'SUCCESS') {
        sucMsg.fadeIn(100);
      } else {
        errMsg.fadeIn(100);
      }
    });
  }
});
