const form = $('#main form');
const errSpan = $('#errMessage');

form.submit((e) => {
  e.preventDefault();

  // [0] = Username || [1] = Password
  const content = $('#main form div input');
  const postData = { username: content[0].value, password: content[1].value };

  CheckLogin(postData, true).then((x) => {
    if (x == true) location.href = 'menu.html';
    else {
      errSpan.text('');

      if (x == 'ACCESS_DENIED')
        errSpan.append('Se han intentado demasiados login. Reincie la API para reiniciar.');
      else errSpan.append('Usuario o contraseña incorrectos.');

      errSpan.fadeIn();
    }
  });
});
