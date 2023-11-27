function applyStyles() {
    const fontSize = $('#fontSize').val() + 'px';
    const textColor = $('#textСolor').val();
    const bgColor = $('#bgColor').val();

    // Применяем стили к элементам страницы
    $('body').css({
        'font-size': fontSize,
        'color': textColor,
    });

    $('.article').css('background-color', bgColor);
    $('#article_short_content').css('color', textColor);
}