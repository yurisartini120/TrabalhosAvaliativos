
function criarBoletim() {
    const boletimTableBody = document.getElementById("boletimTableBody");
  
    const rowAluno = document.createElement("tr");
    rowAluno.innerHTML = `<th rowspan="${disciplinas.length + 2}">${aluno.nome}</th>`;
    boletimTableBody.appendChild(rowAluno);
  
    disciplinas.forEach((disciplina, index) => {
      const rowDisciplina = document.createElement("tr");
      rowDisciplina.innerHTML = `
        <td>${disciplina}</td>
        ${aluno.notas[index].map(nota => `<td>${nota}</td>`).join('')}
        <td>${aluno.notas[index].reduce((total, nota) => total + nota, 0)}</td>
        <td>${(aluno.notas[index].reduce((total, nota) => total + nota, 0) / aluno.notas[index].length).toFixed(2)}</td>
        <td class="${definirStatus(aluno.notas[index].reduce((total, nota) => total + nota, 0))}">${definirStatus(aluno.notas[index].reduce((total, nota) => total + nota, 0))}</td>
      `;
      boletimTableBody.appendChild(rowDisciplina);
    });
  
    const rowTotal = document.createElement("tr");
    const somaTotal = calcularSomaBimestres(aluno.notas);
    const mediaTotal = (calcularSomaBimestres(aluno.notas) / (aluno.notas.length * aluno.notas[0].length)).toFixed(2);
    rowTotal.innerHTML = `
      <th>Total</th>
      ${aluno.notas[0].map((_, index) => `<th>${aluno.notas.reduce((sum, bimestres) => sum + bimestres[index], 0)}</th>`).join('')}
      <th>${somaTotal}</th>
      <th>${mediaTotal}</th>
      <th class="${definirStatus(somaTotal)}">${definirStatus(somaTotal)}</th>
    `;
    boletimTableBody.appendChild(rowTotal);
  }
  
  criarBoletim();
  