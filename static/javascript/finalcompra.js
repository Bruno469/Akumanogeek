function buscaEndereco(cep) {
    if (cep.length !== 8) {
      alert('CEP inválido, tente novamente');
      return;
    }
  
    const url = `https://viacep.com.br/ws/${cep}/json/`;
  
    // Realiza a requisição e trata a resposta
    fetch(url)
      .then(response => response.json())
      .then(data => {
        if (data.erro) {
          alert('CEP não encontrado!');
          return;
        }
  
        // Aqui você tem acesso aos dados do endereço
        console.log(data);
        // Exemplo: atualizar os campos com os dados
        document.querySelector('#cidade').value = data.localidade;
        document.querySelector('#bairro').value = data.bairro;
        document.querySelector('#rua').value = data.logradouro;
        document.querySelector('#estado').value = data.uf;
      })
      .catch(error => console.error('Falha na requisição', error));
  }
  
  // Adiciona um evento para buscar o endereço quando o CEP for digitado
  document.addEventListener('DOMContentLoaded', () => {
    const inputCep = document.querySelector('input[placeholder="Insira seu CEP"]');
    inputCep.addEventListener('blur', (event) => {
      const cep = event.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
      buscaEndereco(cep);
    });
  });

function
validarFormulario() {

  const 

  camposObrigatorios =
  document.querySelectorAll('input[required]');
  for (let campo of camposObrigatorios) {
  if
  (!campo.value.trim()) {
  alert('preencha todos os campos');
  return false;
  }
}

  const
  metodoEntregaSelecionado =
  document.querySelector('input[name="entrega"]:checkded');
  if
  (!metodoEntregaSelecionado) {
    alert('escolha um metodo de entrega');
    return false;

  }
 return true

  }

              // Restante do código da função
              if (data.erro) {
                // Exibe a mensagem de erro
                document.getElementById('cep-error').style.display = 'block';
                return;
              }
             else {
                // Esconde a mensagem de erro se o CEP for válido
                document.getElementById('cep-error').style.display = 'none';
              }
        
      
        // Sua função validarFormulario modificada
        function validarFormulario() {
            // Restante do código da função
            // Verifica se o campo CEP possui valor informado e se é válido
            const cep = document.getElementById('cep').value.replace(/\D/g, '');
            if (cep.length !== 8 || document.getElementById('cep-error').style.display === 'block') {
                // Mantém a mensagem de erro visível se o CEP for inválido
                document.getElementById('cep-error').style.display = 'block';
                return false;
            }
            // Restante do código da função
        }