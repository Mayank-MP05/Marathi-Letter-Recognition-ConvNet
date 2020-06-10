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
  console.log("Reset BG called");
  simpleBoard.resetBackground();
};

const GetImageURL = () => {
  url = simpleBoard.getImg();
  console.log("Image Request Sent ...");
  $.ajax({
    type: "POST",
    url: "/upload",
    data: {
      imageBase64: url,
    },
  }).done(function (e) {
    updateTable(e);
    ResetBG();
    console.log(e);
  });
};
