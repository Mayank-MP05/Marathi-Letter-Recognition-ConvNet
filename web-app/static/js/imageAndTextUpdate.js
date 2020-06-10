const updateTable = (obj) => {
  console.log("Update Table called");

  const imgParent = document.getElementById("current-img");
  const predictParent = document.getElementById("current-prediction");

  imageID = obj.imageID;
  prediction = obj.prediction;

  url = `http://localhost:5000/image/${imageID}`;
  img = `<img src="${url}" class="thumb-img">`;

  imgParent.innerHTML = img;
  predictParent.innerHTML = prediction;
};
