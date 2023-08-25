// Função para calcular a média

function calcularMedia(notas) {

  return notas.reduce((sum, nota) => sum + nota, 0) / notas.length;

}



// Função para determinar a situação do aluno

function verificarSituacao(media) {

  if (media >= 15.0) {

    return 'rgb(0, 128, 0) Aprovado';

  } else if (media >= 10.0) {

    return 'rgb(255, 255, 0)  Recuperação';

  } else {

    return 'rgb(255, 0, 0) Reprovado';

  }

}



// Lista de alunos

let listaAlunos = [];



while (true) {

  let nomeAluno = prompt("Digite o nome do aluno (ou 0 para sair):");



  if (nomeAluno === "0") {

    break; // Encerrar o loop quando for digitado "0"

  }



  let notas = {

    Matemática: [],

    Português: [],

    Física: [],

    Química: [],

    Biologia: []

  };



  for (let bimestre = 1; bimestre <= 4; bimestre++) {

    for (let disciplina in notas) {

      let nota = parseFloat(prompt('Digite a nota de ' + disciplina + ' no ' + bimestre + 'º bimestre para o aluno ' + nomeAluno + ': ' ));

      notas[disciplina].push(nota);

    }

  }



  let aluno = {

    nome: nomeAluno,

    notas: notas

  };



  listaAlunos.push(aluno);

}



// Exibir resultados

for (let aluno of listaAlunos) {

  document.write( '<br>' + '<br>' + 'Aluno:  ' + aluno.nome);

  for (let disciplina in aluno.notas) {

    let mediaDisciplina = calcularMedia(aluno.notas[disciplina]);

    let situacao = verificarSituacao(mediaDisciplina);

    document.write('</br> '  + disciplina + ':    ' + '    Média   ' + mediaDisciplina.toFixed(2) + '  Situação:    ' + situacao );

  }

}

