let session = GetSessionLogin() ?? null;
if (!session) GoToIndex();

CheckLogin(session).then((x) => {
  if (x == true) {
    // TODO:
  } else GoToIndex();
});

$('#editSection').fadeOut();

const errMsg = $('#errMessage');
const sucMsg = $('#sucMessage');
const errMsg2 = $('#errMessage2');

$('#inputId').on('input', () => {
  $('#editSection').fadeOut(100);
  $('#inputNombre').value = '';
  $('#inputApellido').value = '';
  $('#inputEdad').value = '';
});

// * GET
$('#btnSearch').click(() => {
  session.dni = $('#inputId')[0]?.value;
  if (session.dni) {
    errMsg.fadeOut(100);
    errMsg2.fadeOut(100);
    sucMsg.fadeOut(100);

    $.jpost('obtenerPaciente', session).then((res) => {
      res = res.split(',');

      const resNombre = res[1];
      const resApellido = res[2];
      const resEdad = res[3];
      const resDni = res[4]?.slice(0, -2) ?? null;

      console.log(res);
      if (session.dni == resDni) {
        $('#editSection').fadeIn(100);
        $('#editHeader').text(`Editar paciente (${resNombre} ${resApellido})`);

        $('#inputNombre').val(resNombre);
        $('#inputApellido').val(resApellido);
        $('#inputEdad').val(resEdad);
      } else {
        errMsg.fadeIn(100);
      }
    });
  }
});

// * EDIT
$('#btnAdd').click(() => {
  session.nombre = $('#inputNombre')[0]?.value;
  session.apellido = $('#inputApellido')[0]?.value;
  session.edad = $('#inputEdad')[0]?.value;
  session.dni = $('#inputId')[0]?.value;

  if (session.nombre && session.apellido && session.edad && session.dni) {
    errMsg.fadeOut(100);
    errMsg2.fadeOut(100);
    sucMsg.fadeOut(100);

    $.jpost('modificarPaciente', session).then((res) => {
      if (res == 'SUCCESS') {
        sucMsg.fadeIn(100);
      } else {
        errMsg2.fadeIn(100);
      }
    });
  }
});
