<html>
    <head>
    <title>ViaCEP Webservice</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <!-- Adicionando Javascript -->
    <script>
    
    function limpa_formulário_cep() {
            //Limpa valores do formulário de cep.
            document.getElementById('rua').value=("");
            document.getElementById('bairro').value=("");
            document.getElementById('cidade').value=("");
            document.getElementById('uf').value=("");
            document.getElementById('ibge').value=("");
    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('rua').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('cidade').value=(conteudo.localidade);
            document.getElementById('uf').value=(conteudo.uf);
            document.getElementById('ibge').value=(conteudo.ibge);
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }
        
    function pesquisacep(valor) {

        //Nova variável "cep" somente com dígitos.
        var cep = valor.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('rua').value="...";
                document.getElementById('bairro').value="...";
                document.getElementById('cidade').value="...";
                document.getElementById('uf').value="...";
                document.getElementById('ibge').value="...";

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    };

    </script>
    </head>

    <body>
    <!-- Inicio do formulario -->
      <form method="post" action="{{route('update',$cliente[0]->id)}}">
        @csrf
        <label>Nome:
            <input name="nome" type="text" value="{{$cliente[0]->name}}"  id="nome" size="60" /></label><br />
            <label>Telefone:
            <input name="telefone" type="text" value="{{$cliente[0]->telefone}}"  id="telefone" size="40" /></label><br />
            <label>Email:
            <input name="email" type="text" value="{{$cliente[0]->email}}"  id="email" size="40" /></label><br />
        <label>Cep:
        <input name="cep" type="text" value="{{$cliente[0]->cep}}"  id="cep" value="" size="10" maxlength="9"
               onblur="pesquisacep(this.value);" /></label><br />
        <label>Rua:
        <input name="rua" type="text" value="{{$cliente[0]->rua}}" id="rua" size="60" /></label><br />
        <label>Barrio:
        <input name="barrio" type="text" value="{{$cliente[0]->barrio}}"  id="barrio" size="40" /></label><br />
        <label>Cidade:
        <input name="cidade" type="text" value="{{$cliente[0]->cidade}}"  id="cidade" size="40" /></label><br />
        <label>Estado:
        <input name="uf" type="text"value="{{$cliente[0]->estado}}"  id="uf" size="2" /></label><br />
        <label>Numero:
        <input name="numero" type="text"value="{{$cliente[0]->numero}}"  id="numero" size="8" /></label><br />
        <label>Complemento:
        <input name="complemento" type="text" value="{{$cliente[0]->complemento}}"  id="complemento" size="8" /></label><br />
        <label>Pais:
        <input name="pais" type="text" value="{{$cliente[0]->pais}}"  id="pais" size="8" /></label><br />
        <button type="subimit" class="btn btn-primary">Primary</button>
      </form>
    </body>

    </html>