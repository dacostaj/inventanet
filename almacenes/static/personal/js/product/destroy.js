$(document).ready(function(){

        $('.btn-destroy').click(function(e){ // funcion que escucha los click del boton destroy
         e.preventDefault();	
         
         var id = $(this).val();  // tomo el valor que tiene cada boton edit
         var row = $(this).parents('tr');
         row.fadeOut();
         $.ajax({

          url: 'product/delete',
          type: 'GET',
          data: {'id': id},
          
          success: function(result){
            console.log(result.mensaje)
            tpl = '<div class="alert alert-info alert-dismissible">'
                  +'<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>'
                  +'<h4><i class="icon fa fa-info"></i> Información!</h4>'+result.mensaje+'</div>';
          $('#alerta').html(tpl) //puedes usar before o after si lo quieres posicionar con respecto a otro elemento
          
          }
          })
         

         
        }); //fin función btn-destroy


});