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
    sendDataToServer(selectedValues);
  });
});

function sendDataToServer(data) {
  $.ajax({
    url: "/process-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      $("#promptText").text(response.message);
      console.log(response);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      console.log(textStatus);
    },
  });
}
