like = (id)=>{
    $.get('/like/'+id,(newlikes)=>{
        $("#likespan"+id).text(newlikes)
    });
};
