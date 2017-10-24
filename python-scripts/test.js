var scr = document.createElement("script");
scr.src = "https://code.jquery.com/jquery-1.9.1.min.js";
document.body.appendChild(scr);



let daBlock = [];

$('a.style-scope.ytd-playlist-video-renderer[is="yt-endpoint"]').each(function(index) {
    let daString;
    
    let ytId = $(this).attr('href').slice(9, 20);
    let title = $.trim($(this).find('#video-title').html());
    

    daString = `
        $trailer${index} = new SiteVideo([
            'site_id' => $siteId,
            'order' => ${index},
            'title' => '${title}',
            'yt_id' => '${ytId}',
            'description' => '',
            'shareable_twitter' => true,
            'shareable_facebook' => true,
            'shareable_instagram' => true 
        ]);
        $trailer${index}->save();
    `;

    console.log(daString);

    daBlock.push(daString);
});

console.log(daBlock);


// $firstTrailer = new SiteVideo([
//     'site_id' => $siteId,
//     'order' => 0,
//     'title' => 'Official Trailer',
//     'yt_id' => 'C_bfOWof0Sg',
//     'description' => '',
//     'shareable_twitter' => true,
//     'shareable_facebook' => true,
//     'shareable_instagram' => true
// ]);
// $firstTrailer->save();