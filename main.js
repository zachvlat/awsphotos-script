const sizes = ["2", "3", "4", "5", "6", "7", "1F", "2F"];

function deployPhotoString() {
  const photoCode = document.getElementById("photoCode").value;
  const sizeCode = document.getElementById("sizeCode").value;

  let selectedSizes = [];
  if (sizeCode.toLowerCase() === "all") {
    selectedSizes = sizes;
  } else {
    selectedSizes = [sizeCode];
  }

  const table = document.getElementById("photoTable");
  table.innerHTML = "";

  selectedSizes.forEach((size) => {
    const row = table.insertRow();
    const cell1 = row.insertCell();
    const cell2 = row.insertCell();
    const cell3 = row.insertCell();
    const cell4 = row.insertCell();

    cell1.innerHTML = `<pre>/verybig/${photoCode}@${size}.JPG\n</pre>`;
    cell2.innerHTML = `<pre>/verybig/${photoCode}@${size}.jpg\n</pre>`;
    cell3.innerHTML = `<pre>/small/${photoCode}@${size}.JPG\n</pre>`;
    cell4.innerHTML = `<pre>/small/${photoCode}@${size}.jpg\n</pre>`;
  });
}

function clearAll() {
  const table = document.getElementById("photoTable");
  table.innerHTML = "<thead><tr><th></th></tr></thead><tbody></tbody>";
}
