//all buttons lose opacity on click
const btns = document.querySelectorAll('button');

for (btn of btns) {
  btn.addEventListener('mousedown', function() {
    this.classList.add("clicked");
  });

  btn.addEventListener('mouseup', function() {
    this.classList.remove("clicked");
  });
}

//seed list button variables
const uriButton = document.getElementById('uriButton');
const clearButton = document.getElementById('clearButton')

let form = document.getElementById('info');
const uriList = document.getElementById('seedListArea');
let uriInputText = "";

let uriCounter = 0;
const uriArray = []; 

function addUri(e){
  //add more input validation
  //prevent default stops form from updating
  e.preventDefault();

  var currentInputValue = String(form.uriInputID.value);
  var newUriListItem = document.createElement('li');
  
  if(currentInputValue.substring(0,14) == "spotify:track:"){
    newUriListItem.classList.add('realURI');
    newUriListItem.setAttribute("id", "URI "); //MAKE ID DYNAMIC OR REMOVE ALLTOGETHER
    newUriListItem.appendChild(document.createTextNode(currentInputValue));
    uriList.appendChild(newUriListItem);

    uriArray.push(currentInputValue);
    //alert(uriArray);

    uriCounter++;
    form.uriInputID.value = "";  
  }

  else{
    form.uriInputID.value = "";
    let text = document.getElementById("seedListArea").firstChild.text;
    alert("The URI that was entered is invalid.");
  }

}

function clearList(e){

  e.preventDefault();

  while(uriList.firstChild){
    uriList.removeChild(uriList.firstChild);
  }
}

uriButton.addEventListener("click", addUri);
clearButton.addEventListener("click",clearList)


//const forum = document.getElementByID('form1');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  alert("wirked");    // prevent page from refreshing
  const formData = new FormData(form);  // grab the data inside the form fields
  fetch('/play', {   // assuming the backend is hosted on the same server
      method: 'POST',
      body: formData,
  }).then(function(response) {
      // do something with the response if needed.
      // If you want the table to be built only after the backend handles the request and replies, call buildTable() here.
  });
});

//remove form from div and then empty list for clear button, form cant be in list
