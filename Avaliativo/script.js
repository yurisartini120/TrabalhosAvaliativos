function calcularNota() {
    var nomeAluno = document.getElementById("nomeAluno").value;

    var notas = [];

    var disciplina = ['Matematica', 'Portugues', 'Fisica', 'Quimica', 'Biologia'];

    var bimestre = [10, 20, 30, 40];

    var resultado = document.getElementById("resultado");
    resultado.innerHTML = '';

    for (var i = 0; i < disciplina.length; i++) {
        var disciplinaNotas = [];

        for (var j = 0; j < bimestre.length; j++) {
            var nota = parseFloat(prompt("Digite a nota da disciplina " + disciplina[i]));
            disciplinaNotas.push(nota);
        }

        notas.push(disciplinaNotas);

        var somaNotas = notas[i].reduce((total, nota) => total + nota, 0);
        var media = somaNotas / bimestre.length;

        var recuperacao = '';
        if (media <= 40) {
            recuperacao = 'Reprovado';
        } else if (media <= 60) {
            recuperacao = 'Recuperação';
        } else {
            recuperacao = 'Aprovado';
        }

        var resultadoDisciplina = document.createElement("p");
        resultadoDisciplina.innerHTML = disciplina[i] + " - " + media + " - " + recuperacao;
        resultado.appendChild(resultadoDisciplina);
    }
}