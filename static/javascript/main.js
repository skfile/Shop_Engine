$("#search-button").click(function () {
    var str = $("#header-search").val();
    window.location.href("/search/" + str)
});