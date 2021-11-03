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
const tableHead = $('thead');
const errMsg = $('#errMessage');
$('#btnSearch').click(() => {
  session.dni = $('#inputDni')[0]?.value;
  if (session.dni) {
    tableBody.empty();
    tableHead.empty();
    errMsg.fadeOut(100);

    $.jpost('buscarTurnoSegunDni', session).then((res) => {
      if (res != 'NOT_FOUND' || !res) {
        res = res.split(';');

        tableHead.append(`
          <tr>
            <th>ID</th>
            <th>Paciente</th>
            <th>Fecha</th>
            <th>Hora</th>
          </tr>
        `);

        res.forEach((t) => {
          const turno = new Turno(t.split(','));
          console.log(turno);

          tableBody.append(`
            <tr>
              <td>${turno.id}</td>
              <td>${turno.idPaciente}</td>
              <td>${turno.fecha}</td>
              <td>${turno.hora}</td>
            </tr>
          `);
        });
      } else {
        // TODO: NOT FOUND
        errMsg.fadeIn(100);
      }
    });
  }
});
