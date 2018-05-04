$(document).ready(function(){
        
        $('.btn-edit').click(function(){ // funcion que escucha los click del boton edit

         var id = $(this).val();  // tomo el valor que tiene cada boton edit
         var row = $(this).parents('tr');   
       

         $('#'+id).on('submit', function(e){ // funcion que escucha los click del boton update
          e.preventDefault();
          
         $.ajax({

          url: $(this).attr('action'),
          type: $(this).attr('method'),
          data: $(this).serialize(),
          
          success: function(result){

            console.log(result)
            
         $('#modal-update-'+id).modal('hide');
          
          tpl = '<div class="alert alert-info alert-dismissible">'
                  +'<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>'
                  +'<h4><i class="icon fa fa-info"></i> Información!</h4>'+result.mensaje+'</div>';
          $('#alerta').html(tpl) //puedes usar before o after si lo quieres posicionar con respecto a otro elemento
          
          row.find('td').eq(1).text(result.name);
          row.find('td').eq(2).text(result.description);
          }
          })  // fin de envio de dato ajax
         
         
        }); //fin función btn-actualizar


         
        }); //fin función btn-edit


      });
