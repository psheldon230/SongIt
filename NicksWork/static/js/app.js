$(document).ready(function () {
  $("#returnDataPython").click(function () {
    const selectEl = document.getElementById("selectSongs");
    console.log(selectEl);
    const selectedValues = [];
    for (let i = 0; i < selectEl.options.length; i++) {
      if (selectEl.options[i].selected) {
        selectedValues.push(selectEl.options[i].value);
      }
    }
    console.log(selectedValues);
    var responce = sendDataToServer(selectedValues);
    console.log("nick" + responce);
  });
});
function formatTextForHTML(text) {
  // Replace newline characters with HTML line breaks
  // const formattedText = text.replace(/\n/g, "<br>");
  // const formattedText = text
  var formattedText = text
  return formattedText

  // Replace consecutive whitespace characters with non-breaking spaces
  return formattedText.replace(/[\s]+/g, "&nbsp;");
}

function sendDataToServer(data) {
  $.ajax({
    url: "/process-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      console.log(response.message)

      $("#promptText").text(response.message);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      console.log(textStatus);
    },
  });
}
