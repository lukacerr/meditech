let session = GetSessionLogin() ?? null;
if (!session) GoToIndex();

CheckLogin(session).then((x) => {
  if (x == true) {
    // TODO:
  } else GoToIndex();
});

class Paciente {
  constructor(splitedArray) {
    this.id = Number(splitedArray[0]);
    this.nombre = splitedArray[1].charAt(0).toUpperCase() + splitedArray[1].slice(1);
    this.apellido = splitedArray[2].charAt(0).toUpperCase() + splitedArray[2].slice(1);
    this.edad = Number(splitedArray[3]);
    this.dni = splitedArray[4];
  }
}

const tableBody = $('tbody');
$.jpost('listarPacientes', session).then((res) => {
  res.forEach((p) => {
    const paciente = new Paciente(p.split(','));

    tableBody.append(`
      <tr>
        <td>${paciente.id}</td>
        <td>${paciente.nombre}</td>
        <td>${paciente.apellido}</td>
        <td>${paciente.edad}</td>
        <td>${paciente.dni}</td>
      </tr>
    `);
  });
});

const errMsg = $('#errMessage');
const sucMsg = $('#sucMessage');
$('#btnAdd').click(() => {
  session.nombre = $('#inputNombre')[0]?.value;
  session.apellido = $('#inputApellido')[0]?.value;
  session.edad = $('#inputEdad')[0]?.value;
  session.dni = $('#inputDni')[0]?.value;

  if (session.nombre && session.apellido && session.edad && session.dni) {
    errMsg.fadeOut(100);
    sucMsg.fadeOut(100);

    $.jpost('agregarPaciente', session).then((res) => {
      if (res == 'SUCCESS') {
        sucMsg.fadeIn(100);
        tableBody.empty();

        $.jpost('listarPacientes', session).then((res) => {
          res.forEach((p) => {
            const paciente = new Paciente(p.split(','));

            tableBody.append(`
              <tr>
                <td>${paciente.id}</td>
                <td>${paciente.nombre}</td>
                <td>${paciente.apellido}</td>
                <td>${paciente.edad}</td>
                <td>${paciente.dni}</td>
              </tr>
            `);
          });
        });
      } else {
        errMsg.fadeIn(100);
      }
    });
  }
});
