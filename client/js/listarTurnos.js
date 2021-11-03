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
    /*
    this.id = Number(splitedArray[0]);
    this.nombre = splitedArray[1].charAt(0).toUpperCase() + splitedArray[1].slice(1);
    this.apellido = splitedArray[2].charAt(0).toUpperCase() + splitedArray[2].slice(1);
    this.edad = Number(splitedArray[3]);
    this.dni = splitedArray[4];¨
    */
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
