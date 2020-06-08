var simpleBoard = new DrawingBoard.Board("simple-board", {
  controls: false,
  background: "#000",
  color: "#fff",
  size: 20,
  webStorage: false,
});
//simpleBoard.addControl("Download"); //if the DrawingBoard.Control.Download class exists

//listen to an event
simpleBoard.ev.bind("board:reset", why);

//stop listening to it

simpleBoard.ev.unbind("board:reset", why);

function why() {
  alert("OH GOD WHY");
}

const ResetBG = () => {
  console.log(simpleBoard);
  simpleBoard.resetBackground();
};

const GetImageURL = () => {
  url = simpleBoard.getImg();
  console.log(url);
  formData = new FormData();
  formData.append("imagedata", url);
  /*
    $.ajax({
      url: "/upload",
      type: "POST",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
    }).done(function (e) {
      alert(e);
    });
  */
  $.ajax({
    type: "POST",
    url: "/hook",
    data:{
      imageBase64: url
    }
  }).done(function() {
    console.log('sent');
  });
};
