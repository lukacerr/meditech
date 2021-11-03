let session = GetSessionLogin() ?? null;
if (!session) GoToIndex();

CheckLogin(session).then((x) => {
  if (x == true) {
    // TODO:
  } else GoToIndex();
});

class Turno {
  constructor(splitedArray) {
    this.id = splitedArray[0];
    this.idPaciente = splitedArray[1];
    this.fecha = splitedArray[2];
    this.hora = splitedArray[3];
  }
}

const tableBody = $('tbody');
$.jpost('listarTurnos', session).then((res) => {
  res.forEach((t) => {
    const turno = new Turno(t.split(','));

    tableBody.append(`
      <tr>
        <td>${turno.id}</td>
        <td>${turno.idPaciente}</td>
        <td>${turno.fecha}</td>
        <td>${turno.hora}</td>
      </tr>
    `);
  });
});

const errMsg = $('#errMessage');
const sucMsg = $('#sucMessage');
$('#btnAdd').click(() => {
  session.paciente = $('#inputDni')[0]?.value;
  session.fecha = $('#inputFecha')[0]?.value;
  session.hora = $('#inputHora')[0]?.value;

  if (session.paciente && session.fecha && session.hora) {
    errMsg.fadeOut(100);
    sucMsg.fadeOut(100);

    $.jpost('agregarTurno', session).then((res) => {
      if (res == 'SUCCESS') {
        sucMsg.fadeIn(100);
        tableBody.empty();

        $.jpost('listarTurnos', session).then((res) => {
          res.forEach((t) => {
            const turno = new Turno(t.split(','));

            tableBody.append(`
              <tr>
                <td>${turno.id}</td>
                <td>${turno.idPaciente}</td>
                <td>${turno.fecha}</td>
                <td>${turno.hora}</td>
              </tr>
            `);
          });
        });
      } else {
        switch (res) {
          case 'DNI_INVALID':
            res = 'el documento introducido no existe o no es válido';
            break;
          case 'DATE_INVALID':
            res = 'la fecha introducida no es válida';
            break;
          case 'TIME_INVALID':
            res = 'la hora introducida no es válida';
            break;
          case 'DATE_DISABLED':
            res = 'los días 1, 8, 15 y 22 no están disponibles';
            break;
          case 'TIME_DISABLED':
            res = 'solamente están habilitados los horarios de 10 AM a 2 PM';
            break;
          default:
            res = 'excepción no controlada';
            break;
        }

        errMsg.text('Error de validación o desconocido (' + res + ').');
        errMsg.fadeIn(100);
      }
    });
  }
});
