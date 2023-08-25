const alunos = [
    { nome: "João", notas: [10, 10, 10, 10] },
    { nome: "Maria", notas: [72, 65, 55, 80] },
    { nome: "Pedro", notas: [40, 35, 42, 60] },
    // Adicione mais alunos aqui se necessário
  ];
  
  function calcularMedia(notas) {
    return notas.reduce((sum, nota) => sum + nota, 0) / notas.length;
  }
  
  function definirStatus(media) {
    if (media >= 60) {
      return "Aprovado";
    } else if (media >= 40) {
      return "Recuperação";
    } else {
      return "Reprovado";
    }
  }
  
  function exibirBoletim() {
    const tableBody = document.getElementById("boletimTableBody");
  
    alunos.forEach(aluno => {
      const media = calcularMedia(aluno.notas);
      const status = definirStatus(media);
  
      const newRow = tableBody.insertRow();
      newRow.innerHTML = `
        <td>${aluno.nome}</td>
        <td>${aluno.notas[0]}</td>
        <td>${aluno.notas[1]}</td>
        <td>${aluno.notas[2]}</td>
        <td>${aluno.notas[3]}</td>
        <td>${media.toFixed(2)}</td>
        <td class="${status.toLowerCase()}">${status}</td>
      `;
    });
  }
  
  exibirBoletim();
  