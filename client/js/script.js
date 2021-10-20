const BackURL = 'http://localhost:8000';

const RequestAPI = async (call, params) => {
   const rq = `${BackURL}${call}`;

   if (params) {
      var xhr = new XMLHttpRequest();
      xhr.open('POST', rq);

      xhr.setRequestHeader('Accept', 'application/json');
      xhr.setRequestHeader('Content-Type', 'application/json');

      xhr.send(JSON.stringify(params));

      xhr.onreadystatechange = function () {
         if (xhr.readyState === 4) {
            return JSON.parse(xhr.responseText);
         }
      };
   } else {
      const response = await fetch(rq);
      const data = await response.json();
      return data;
   }
};

function Login() {
   const username = document.getElementById('username').value;
   const password = document.getElementById('password').value;

   console.log({ username, password });

   RequestAPI('/login', { username, password }).then((x) => console.log(x));
}

// RequestAPI('/').then((x) => console.log(x));
