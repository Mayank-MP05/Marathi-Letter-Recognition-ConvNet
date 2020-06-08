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
  $.ajax({
    type: "POST",
    url: "/upload",
    data: {
      imageBase64: url,
    },
  }).done(function (e) {
    console.log("Image Request Sent ...");
    console.log(e);
  });
};
