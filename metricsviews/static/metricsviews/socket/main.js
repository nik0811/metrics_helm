var socket = new WebSocket(
            'ws://'
            + window.location.host
            + '/api/view/clustersock/'
        );

socket.onmessage = function(e){
     var socketData = JSON.parse(e.data);
     console.log(socketData)

     document.querySelector('#app').innerText = socketData.value;
}
