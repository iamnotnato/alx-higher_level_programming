$('document').ready(() => {
  const translate = (code) => {
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/`,
      dataType: 'json',
      success: (result) => {
        $('DIV#hello').text(result.hello);
      }
    });
  };

  $('INPUT#btn_translate').on('click', () => {
    const text = $('INPUT#language_code').val();
    translate(text);
  });
});
