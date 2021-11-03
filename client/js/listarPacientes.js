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
