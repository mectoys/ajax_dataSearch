
function Getinformation(button_Ubigeo, cod_text, div_error, des_text){

    document.getElementById(button_Ubigeo).addEventListener('click',function (){
        const DataValue = document.getElementById(cod_text).value;

        //Verificar si el campo está vacio
        // mensaje con div
        if (!DataValue){
            document.getElementById(div_error).style.display='block';
            return;
        }else{
            document.getElementById(div_error).style.display='none';
        }
        //MOSTRAR SPINNER
        const spinner =document.getElementById('loading-spinner');
        spinner.style.display='block';
        //Crear un objeto xmlhttpRequest para realizar la solicitud AJAX

        const xhr = new XMLHttpRequest();
        //Configurar nuestra solicitud
        xhr.open('POST','/getdata', true);

        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function (){
            if(xhr.status == 200){
                const response= JSON.parse(xhr.responseText);
                document.getElementById(des_text).value = response.departamento;
            }
            spinner.style.display='none';
        };
        //construir y enviar los datos al servidor para ser procesado en una solicitud HTTP
        xhr.send('codubigeo=' + encodeURIComponent(DataValue));
    });
}