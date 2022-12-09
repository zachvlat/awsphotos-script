function deployPhotoString() {
  let photoCode = document.getElementById("photoCode").value;

  let table = document
    .getElementById("photoTable")
    .getElementsByTagName("tbody")[0];

  let newRow = table.insertRow();
  let titleCell = newRow.insertCell(0);

  let photoNode = document.createTextNode(photoCode);
  let photoBig = document.createTextNode("/verybig/");
  let photoSmall = document.createTextNode("/small/");
  let jpg = document.createTextNode(".jpg");
  let jpgBig = document.createTextNode(".JPG");
  let four = document.createTextNode("@4");
  let five = document.createTextNode("@5");
  let six = document.createTextNode("@6");
  let oneF = document.createTextNode("@1F");
  let twoF = document.createTextNode("@2F");

  titleCell.append(photoBig) +
    titleCell.append(photoNode) +
    titleCell.append(four) +
    titleCell.append(jpg);
}

function clearAll() {
  let clearall = document.getElementById("photoTable").rows;
  while (clearall.length > 0) trs[0].parentNode.removeChild(trs[0]);
}
