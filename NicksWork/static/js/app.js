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
    var textarea = document.querySelector('textarea[name="textbox"]');
    var text = textarea.value;
    console.log(text);
    // Prepare the data to be sent to the server
    var data = {
      selectedValues: selectedValues,
      text: text,
    };

    // Send the data to the server
    var response = sendDataToServer(data);
    $("#promptText").text("Loading Please Wait");
  });

  $("#updateSongButton").click(function () {
    // Get the updated instructions from the textarea
    const updatedInstructions = document.getElementById("updateSong").value;

    // Get the previous song from the pre element
    const previousSong = document.getElementById("promptText").textContent;

    // Combine the variables into a single object
    const data = {
      updatedInstructions: updatedInstructions,
      previousSong: previousSong,
    };
    $("#promptText").text("Loading Please Wait");
    sendDataToServerUpdateSong(data)
  });

  $("#selectSongs").change(function () {
    // your code here
    const selectEl = document.getElementById("selectSongs");
    const selectedValues = [];
    for (let i = 0; i < selectEl.options.length; i++) {
      if (selectEl.options[i].selected) {
        selectedValues.push(selectEl.options[i].value);
      }
    }
    sendSelectedAlbumsToServer(selectedValues);
  });
});
function formatTextForHTML(text) {
  // Replace newline characters with HTML line breaks
  // const formattedText = text.replace(/\n/g, "<br>");
  // const formattedText = text
  var formattedText = text;
  return formattedText;

  // Replace consecutive whitespace characters with non-breaking spaces
  return formattedText.replace(/[\s]+/g, "&nbsp;");
}

function sendSelectedAlbumsToServer(data) {
  $.ajax({
    url: "/process-album-cover-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      // console.log(response.message);
      console.log(response);
      imageUrls = response.message;
      const boxes = document.querySelectorAll(".containerBottom .box");
      boxes.forEach((box, index) => {
        box.style.backgroundImage = `url(${imageUrls[index]})`;
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      $("#promptText").text("Error sending data");
      console.log(textStatus);
    },
  });
}

function sendDataToServer(data) {
  $.ajax({
    url: "/process-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      console.log(response.message);

      $("#promptText").text(response.message);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      $("#promptText").text("Error sending data");

      console.log(textStatus);
    },
  });
}
function sendDataToServerUpdateSong(data) {
  $.ajax({
    url: "/process-data-update-song",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      console.log(response.message);

      $("#promptText").text(response.message);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      $("#promptText").text("Error sending data");

      console.log(textStatus);
    },
  });
}
