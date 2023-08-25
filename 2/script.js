const disciplinas = ["Matemática", "Português", "Física", "Química", "Biologia"];

let adicionarAluno = true;

 

function obterNotas() {

    const aluno = {

        nome: prompt("Digite o nome do aluno:"),

        notas: []

    };

 

    disciplinas.forEach(disciplina => {

        const notasDisciplina = [];

        for (let i = 1; i <= 4; i++) {

            notasDisciplina.push(parseInt(prompt(`Digite a nota do ${i}º bimestre em ${disciplina}:`), 10));

        }

        aluno.notas.push(notasDisciplina);

    });

 

    return aluno;

}

 

function calcularSomaBimestres(notas) {

    return notas.reduce((sum, bimestres) => sum + bimestres.reduce((total, nota) => total + nota, 0), 0);

}

 

function definirStatus(somaBimestres) {

    if (somaBimestres >= 60) {

        return "Aprovado";

    } else if (somaBimestres >= 40) {

        return "Recuperação";

    } else {

        return "Reprovado";

    }

}

 

function criarBoletim(aluno) {

    const boletimTableBody = document.getElementById("boletimTableBody");

    const rowAluno = document.createElement("tr");

    rowAluno.innerHTML = `<th rowspan="${disciplinas.length + 1}">${aluno.nome}</th>`;

    boletimTableBody.appendChild(rowAluno);

 

    disciplinas.forEach((disciplina, index) => {

        const rowDisciplina = document.createElement("tr");

        const somaNotas = aluno.notas[index].reduce((total, nota) => total + nota, 0);

        const status = definirStatus(somaNotas);

        rowDisciplina.innerHTML = `

            <td>${disciplina}</td>

            ${aluno.notas[index].map(nota => `<td>${nota}</td>`).join('')}

            <td>${somaNotas}</td>

            <td>${(somaNotas / aluno.notas[index].length).toFixed(2)}</td>

            <td class="${status === 'Aprovado' ? 'aprovado' : (status === 'Reprovado' ? 'reprovado' : 'recuperacao')}">${status}</td>

        `;

        boletimTableBody.appendChild(rowDisciplina);

    });

}

 

function adicionarAlunoEBoletim() {

    if (adicionarAluno) {

        const alunoInserido = obterNotas();

        criarBoletim(alunoInserido);

    }

}

 

function pararAdicao() {

    adicionarAluno = false;

}

 

document.getElementById("adicionarAlunoButton").addEventListener("click", adicionarAlunoEBoletim);



adicionarAlunoEBoletim();