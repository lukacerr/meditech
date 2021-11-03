let session = GetSessionLogin() ?? null;
if (!session) GoToIndex();

CheckLogin(session).then((x) => {
  if (x == true) {
    // TODO:
  } else GoToIndex();
});

$('#welcome').text(`Bienvenido, ${session.username}!`);

$('#signOut').click((x) => {
  location.href = './index.html';
  DeleteSessionLogin();
});

// Fix animation
$(function () {
  $('article').css('transition-duration', '0ms');
});

// Routing
$('#altaPaciente').click((x) => {
  location.href = './altaPaciente.html';
});

$('#altaTurno').click((x) => {
  location.href = './altaTurno.html';
});

$('#modificarPaciente').click((x) => {
  location.href = './modificarPaciente.html';
});

$('#listarTurnos').click((x) => {
  location.href = './listarTurnos.html';
});

$('#listarPacientes').click((x) => {
  location.href = './listarPacientes.html';
});

$('#buscarTurnoPorDNI').click((x) => {
  location.href = './buscarTurnoPorDNI.html';
});
