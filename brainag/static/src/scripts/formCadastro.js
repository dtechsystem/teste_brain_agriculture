function getCSRFToken() {
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    return token;
}

function validarCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, '');
    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;
    let soma = 0, resto;
    for (let i = 1; i <= 9; i++) soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) resto = 0;
    if (resto !== parseInt(cpf.substring(9, 10))) return false;
    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) resto = 0;
    if (resto !== parseInt(cpf.substring(10, 11))) return false;
    return true;
  }

function validarCNPJ(cnpj) {
    cnpj = cnpj.replace(/[^\d]+/g, '');
    if (cnpj.length !== 14) return false;
    let tamanho = cnpj.length - 2;
    let numeros = cnpj.substring(0, tamanho);
    let digitos = cnpj.substring(tamanho);
    let soma = 0;
    let pos = tamanho - 7;
    for (let i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2) pos = 9;
    }
    let resultado = soma % 11 < 2 ? 0 : 11 - (soma % 11);
    if (resultado !== parseInt(digitos.charAt(0))) return false;
    tamanho += 1;
    numeros = cnpj.substring(0, tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (let i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2) pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - (soma % 11);
    if (resultado !== parseInt(digitos.charAt(1))) return false;
    return true;
}

function aplicarMascara(valor) {
    valor = valor.replace(/\D/g, ""); // Remove tudo que não é dígito

    if (valor.length <= 11) {
        // Aplicar máscara de CPF
        valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
    } else {
        // Aplicar máscara de CNPJ
        valor = valor.replace(/^(\d{2})(\d)/, "$1.$2");
        valor = valor.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3");
        valor = valor.replace(/\.(\d{3})(\d)/, ".$1/$2");
        valor = valor.replace(/(\d{4})(\d)/, "$1-$2");
    }

    return valor;
}

$("#estado").change(function () {

    const url = "/ajax/buscar-municipios";

    estado = $(this).val();
    $.ajax({
        url: url,
        data: { 'estado': estado},
        success: function (data) {
            $("#cidade").html(data);

        }
    });
  });

  function validarAreas() {
    const areaTotal = parseFloat(document.getElementById('areaTotal').value) || 0;
    const areaAgricultavel = parseFloat(document.getElementById('areaAgricultavel').value) || 0;
    const areaVegetacao = parseFloat(document.getElementById('areaVegetacao').value) || 0;
    
    const somaAreas = areaAgricultavel + areaVegetacao;

    if (somaAreas > areaTotal) {
      Swal.fire({
        icon: 'error',
        title: 'Erro!',
        text: 'A soma da área agricultável e da área de vegetação não pode ser maior que a área total!',
        confirmButtonText: 'OK'
      });

      // Limpa os valores dos campos se a soma ultrapassar a área total
      document.getElementById('areaAgricultavel').value = '';
      document.getElementById('areaVegetacao').value = '';
    }
  }

document.getElementById('cpfCnpj').addEventListener('input', function (e) {
    let valor = e.target.value;
    e.target.value = aplicarMascara(valor);
});

function cadProdutor(){


    const cpfCnpj = document.getElementById('cpfCnpj').value;
    const isValid = validarCPF(cpfCnpj) || validarCNPJ(cpfCnpj);

    if (!isValid) {
        document.getElementById('cpfCnpj').classList.add('is-invalid');
    } else {
        document.getElementById('cpfCnpj').classList.remove('is-invalid');

        const nomeProdutor = document.getElementById('nomeProdutor').value;
        const nomeFazenda = document.getElementById('nomeFazenda').value;
        const cidade = document.getElementById('cidade').value;
        const estado = document.getElementById('estado').value;
        const areaTotal = document.getElementById('areaTotal').value;
        const areaAgricultavel = document.getElementById('areaAgricultavel').value;
        const areaVegetacao = document.getElementById('areaVegetacao').value;
        const culturas = Array.from(document.getElementById('culturas').selectedOptions).map(option => option.value);

        // Criando um objeto com os dados
        var formData = {
          cpfCnpj,
          nomeProdutor,
          nomeFazenda,
          cidade,
          estado,
          areaTotal,
          areaAgricultavel,
          areaVegetacao,
          culturas
        };
   
        // Enviando os dados via jQuery AJAX
        var XCSRFToken = getCSRFToken();
        console.log(formData)
        $.ajax({
            url: '/cadastrar-produtor',
            type: "POST",
            data: {'dados':formData},
            headers: { "X-CSRFToken": XCSRFToken },

            success: function (data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Produtor Cadastrado com sucesso!',
                    text: data.success_message,
                }).then((result) => {
                    // Ação a ser realizada após o botão "OK" ser clicado
                    if (result.isConfirmed) {
                        window.location.href = '/dashboard';
                            
                    }

                });
            },
            error: function (data) {
             
                if (data.responseJSON && data.responseJSON.error_message) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ops!',
                        text: data.responseJSON.error_message
                    });
                }
            }
        });
    }

}

function deletarFazenda(fazendaId) {
    // Usando SweetAlert para confirmação
    
    Swal.fire({
        title: 'Remover Fazenda?',
        text: 'Se remover, todos os registros de culturas plantadas serão removidos!',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
    }).then((result) => {
        if (result.isConfirmed) {
            var XCSRFToken = '{{ csrf_token }}';
            const url = "/remover-fazenda";
            
            // Use a função $.ajax do jQuery para fazer a solicitação AJAX
            $.ajax({
                url: url,
                type: "POST",
                data: { 'fazendaId': fazendaId },
                headers: { "X-CSRFToken": getCSRFToken() },
                success: function (data) {
                    // Remover o acordeon correspondente
                    $('div.panel[data-id="' + fazendaId + '"]').remove();

                    Swal.fire({
                        icon: 'success',
                        title: 'Exclusão Realizada!',
                        text: "A exclusão foi realizada com sucesso!"
                    });
                },
                error: function (data) {
                    console.log(data);
                    if (data.responseJSON && data.responseJSON.error_message) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Ops!',
                            text: data.responseJSON.error_message
                        });
                    }
                }
            });
        }
    });
}

function deletarCultura(culturaId) {


    Swal.fire({
        title: 'Remover Cultura?',
        text: 'Se remover, não poderá ser recuperada!',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
    }).then((result) => {
        if (result.isConfirmed) {
            var XCSRFToken = '{{ csrf_token }}';
            const url = "/remover-cultura";

          
            $.ajax({
                url: url,
                type: "POST",
                data: { 'culturaId': culturaId },
                headers: { "X-CSRFToken": getCSRFToken() }, 
                success: function (data) {
       
                    $('tr[data-cultura-id="' + culturaId + '"]').remove();

                    Swal.fire({
                        icon: 'success',
                        title: 'Solicitação Exclusão!',
                        text: "A exclusão foi realizada com sucesso!"
                    });
                },
                error: function (data) {
                    console.log(data);
                    if (data.responseJSON && data.responseJSON.error_message) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Ops!',
                            text: data.responseJSON.error_message
                        });
                    }
                }
            });
        }
    });
}

function alterarProdutor(id) {

    const cpfCnpj = document.getElementById('cpfCnpj').value;
    const isValid = validarCPF(cpfCnpj) || validarCNPJ(cpfCnpj);
    var produtor_id = id;

    if (!isValid) {
        document.getElementById('cpfCnpj').classList.add('is-invalid');
    } else {
        document.getElementById('cpfCnpj').classList.remove('is-invalid');

        const cpf_cnpj = document.getElementById('cpfCnpj').value;
        const nome_produtor = document.getElementById('produtor_edit').value;
           
        // Enviando os dados via jQuery AJAX
        var XCSRFToken = getCSRFToken();
        $.ajax({
            url: '/editar-produtor',
            type: "POST",
            data: {'produtor_id': produtor_id,'cpfcnpj':cpf_cnpj, 'nome_produtor':nome_produtor},
            headers: { "X-CSRFToken": XCSRFToken },

            success: function (data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Produtor Alterado com sucesso!',
                    text: data.success_message,
                }).then((result) => {
                    // Ação a ser realizada após o botão "OK" ser clicado
                    if (result.isConfirmed) {
                        
                            
                    }

                });
            },
            error: function (data) {
             
                if (data.responseJSON && data.responseJSON.error_message) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ops!',
                        text: data.responseJSON.error_message
                    });
                }
            }
        });
    }



}

function cadFazenda(produtor_id) {
    
        const nomeFazenda = document.getElementById('nomeFazenda').value;
        const cidade = document.getElementById('cidade').value;
        const estado = document.getElementById('estado').value;
        const areaTotal = document.getElementById('areaTotal').value;
        const areaAgricultavel = document.getElementById('areaAgricultavel').value;
        const areaVegetacao = document.getElementById('areaVegetacao').value;
        const culturas = Array.from(document.getElementById('culturas').selectedOptions).map(option => option.value);
        const produtorId = produtor_id;


        // Criando um objeto com os dados
        var formData = {
          nomeFazenda,
          cidade,
          estado,
          areaTotal,
          areaAgricultavel,
          areaVegetacao,
          culturas,
          produtorId
        };
   
        // Enviando os dados via jQuery AJAX
        var XCSRFToken = getCSRFToken();
        console.log(formData)
        $.ajax({
            url: '/cadastrar-fazenda',
            type: "POST",
            data: {'dados':formData},
            headers: { "X-CSRFToken": XCSRFToken },

            success: function (data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Fazenda Cadastrada com sucesso!',
                    text: data.success_message,
                }).then((result) => {
                    // Ação a ser realizada após o botão "OK" ser clicado
                    if (result.isConfirmed) {
                        location.reload(); 
                            
                    }

                });
            },
            error: function (data) {
             
                if (data.responseJSON && data.responseJSON.error_message) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ops!',
                        text: data.responseJSON.error_message
                    });
                }
            }
        });
    }


function showModalView(id) {
    $.ajax({
        url: '/view-produtor/' + id,  // Corrigido para passar o ID na URL
        type: "GET",
        success: function (data) {
            $('#modalView').html(data);
            $('#modalView').modal('show');
        }
    });
    
}

function adicionarCultura(fazenda_id){
   document.getElementById('fazendaIdModal').value = fazenda_id
    console.log('entrou')
    $.ajax({
        url: '/view-culturas/' + fazenda_id,  // Corrigido para passar o ID na URL
        type: "GET",
        success: function (data) {
            $('#culturas_select').html(data);
            $('#modaladdCultura').modal('show');
        }
    });
}
function cadCulturas(){
    fazenda_id = document.getElementById('fazendaIdModal').value
    const culturas = Array.from(document.getElementById('culturas_select').selectedOptions).map(option => option.value);
    console.log(culturas)
    $.ajax({
        url: '/cadastrar-culturas',
        type: "POST",
        data: {'fazenda_id':fazenda_id,'culturas':culturas},
        headers: { "X-CSRFToken": getCSRFToken() },
        success: function (data) {
            Swal.fire({
                icon: 'success',
                title: 'Culturas Cadastradas com sucesso!',
                text: data.success_message,
            }).then((result) => {
                // Ação a ser realizada após o botão "OK" ser clicado
                if (result.isConfirmed) {
                    $('#modaladdCultura').modal('hide');
                    location.reload(); 
                        
                }

            });
        },
        error: function (data) {    
            if (data.responseJSON && data.responseJSON.error_message) {
                Swal.fire({
                    icon: 'error',
                    title: 'Ops!',
                    text: data.responseJSON.error_message
                });
            }
        }
    });
}

function alterarFazenda(id) {

        const nomeFazenda = document.getElementById('nomeFazenda').value;
        const areaTotal = document.getElementById('areaTotal').value;
        const areaAgricultavel = document.getElementById('areaAgricultavel').value;
        const areaVegetacao = document.getElementById('areaVegetacao').value;
        const fazendaId = id;

        // Criando um objeto com os dados
        var formData = {
          nomeFazenda,
          areaTotal,
          areaAgricultavel,
          areaVegetacao,
          fazendaId
        };
        //VERIFICA SE A SOMA DA AGRICULTURA E DA VEGETACAO E MENOR QUE A AREA TOTAL
        var somaAreas = parseFloat(areaAgricultavel) + parseFloat(areaVegetacao);
        if (somaAreas > parseFloat(areaTotal)) {
            Swal.fire({
                icon: 'error',
                title: 'Ops!',
                text: 'A soma da Agricultura e Vegetação deve ser menor que a Area Total'   
            });
            return;
        }
     
        // Enviando os dados via jQuery AJAX
        var XCSRFToken = getCSRFToken();
        console.log(formData)
        $.ajax({
            url: '/editar-fazenda',
            type: "POST",
            data: {'dados':formData},
            headers: { "X-CSRFToken": XCSRFToken },

            success: function (data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Fazenda Alterada com sucesso!',
                    text: data.success_message,
                }).then((result) => {
                    // Ação a ser realizada após o botão "OK" ser clicado
                    if (result.isConfirmed) {
                        location.reload();
                            
                    }

                });
            },
            error: function (data) {
             
                if (data.responseJSON && data.responseJSON.error_message) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ops!',
                        text: data.responseJSON.error_message
                    });
                }
            }
        });
}

function deleteProdutor(id) {
    Swal.fire({
        title: 'Remover Produtor?',
        text: 'Ao remover, removerá todas as fazendas e culturas relacionadas!',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Enviando os dados via jQuery AJAX
            var XCSRFToken = getCSRFToken();
            $.ajax({
                url: '/deletar-produtor',
                type: "POST",
                data: {'id': id},
                headers: { "X-CSRFToken": XCSRFToken },
                success: function (data) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Produtor Removido com sucesso!',
                        text: data.success_message
                    }).then((result) => {
                        // Ação a ser realizada após o botão "OK" ser clicado
                        if (result.isConfirmed) {
                            
                            //remover linha do produtor
                            $('tr[data-id="' + id + '"]').remove();
                                
                        }

                    });
                },
                error: function (data) {
                    if (data.responseJSON && data.responseJSON.error_message) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Ops!',
                            text: data.responseJSON.error_message
                        });
                    }
                }
            });
        }
    })
}

function init_charts(estadosData, culturasData, usoSoloData) {
    // Gráfico por Estado
    if ($("#grafico_estado").length) {
        var ctxEstado = document.getElementById("grafico_estado").getContext("2d");
        var chartEstado = new Chart(ctxEstado, {
            type: "pie",
            data: {
                datasets: [{
                    data: estadosData.totais, // dados passados do Django
                    backgroundColor: ["#455C73", "#9B59B6", "#BDC3C7", "#26B99A", "#3498DB"],
                    label: "Fazendas por Estado"
                }],
                labels: estadosData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }

    if ($("#grafico_estado_user").length) {
        var ctxEstado = document.getElementById("grafico_estado_user").getContext("2d");
        var chartEstado = new Chart(ctxEstado, {
            type: "pie",
            data: {
                datasets: [{
                    data: estadosData.totais, // dados passados do Django
                    backgroundColor: ["#455C73", "#9B59B6", "#BDC3C7", "#26B99A", "#3498DB"],
                    label: "Fazendas por Estado"
                }],
                labels: estadosData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }

    // Gráfico por Cultura
    if ($("#grafico_cultura").length) {
        var ctxCultura = document.getElementById("grafico_cultura").getContext("2d");
        var chartCultura = new Chart(ctxCultura, {
            type: "pie",
            data: {
                datasets: [{
                    data: culturasData.totais, // dados passados do Django
                    backgroundColor: ["#3498DB", "#9B59B6", "#BDC3C7", "#26B99A", "#455C73"],
                    label: "Culturas Plantadas"
                }],
                labels: culturasData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }

    if ($("#grafico_cultura_user").length) {
        var ctxCultura = document.getElementById("grafico_cultura_user").getContext("2d");
        var chartCultura = new Chart(ctxCultura, {
            type: "pie",
            data: {
                datasets: [{
                    data: culturasData.totais, // dados passados do Django
                    backgroundColor: ["#3498DB", "#9B59B6", "#BDC3C7", "#26B99A", "#455C73"],
                    label: "Culturas Plantadas"
                }],
                labels: culturasData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }

    // Gráfico por Uso de Solo
    if ($("#grafico_uso_solo").length) {
        var ctxUsoSolo = document.getElementById("grafico_uso_solo").getContext("2d");
        var chartUsoSolo = new Chart(ctxUsoSolo, {
            type: "pie",
            data: {
                datasets: [{
                    data: usoSoloData.totais, // dados passados do Django
                    backgroundColor: ["#26B99A", "#BDC3C7"],
                    label: "Uso de Solo"
                }],
                labels: usoSoloData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }

    if ($("#grafico_solo_user").length) {
        var ctxUsoSolo = document.getElementById("grafico_solo_user").getContext("2d");
        var chartUsoSolo = new Chart(ctxUsoSolo, {
            type: "pie",
            data: {
                datasets: [{
                    data: usoSoloData.totais, // dados passados do Django
                    backgroundColor: ["#26B99A", "#BDC3C7"],
                    label: "Uso de Solo"
                }],
                labels: usoSoloData.labels // rótulos passados do Django
            },
            options: {
                responsive: true,
                legend: { display: true }
            }
        });
    }
}
    
