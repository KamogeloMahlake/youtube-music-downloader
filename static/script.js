const url = document.getElementById('url');
const downloadType = document.getElementById('downloadtype');
const x = document.getElementById('x');
const loading = document.getElementById('loading');
const main = document.querySelector('main');

document.addEventListener('DOMContentLoaded', async () => {
  if (x.value === "video")
  {
    downloadSong();
  }
  /*else if (x.value === "playlist")
  {
    downloadPlaylist();
  }*/
});

const downloadSong = async () => {
  const i = document.createElement("span");
  i.className = "loading";
  main.appendChild(i);
  let response = await fetch(`/download?url=${url.value}&downloadtype=${downloadType.value}`);
  let data = await response.json();
  main.innerHTML = `<p>${data.message}</p>`;
};

/*
const downloadPlaylist =  async () => {
    let response = await fetch(`playlisturl?url=${url.value}`);
    let videoUrls = await response.json();
    videoUrls.message.forEach(e => {
      let load = document.createElement("span");
      load.className = "loading";
      main.appendChild(load);
      let x = await fetch(`/download?url=${e}&downloadtype=${downloadType.value}`);
      let y = await x.json();
      main.removeChild(load);
      main.innerHTML += `<p>${y.message}</p>`
});
};*/
