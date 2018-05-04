$(document).ready(function(){

var tabla = $('#tablamodaldetalle').DataTable();
 
//
        $('.btn-show').click(function(e){ // funcion que escucha los click del boton destroy
         e.preventDefault();    
         var id = $(this).val();  // tomo el valor que tiene cada boton edit
         var form = $('#form_show');
         var url = form.attr('action').replace(':SHOW_ID', id);
         
         tabla.clear().draw();
           
         
        $.get(url, function(result){

           $('#modalproveedor').html(result.proveedor);
           $('#modaltipoingreso').html(result.tipo_ingreso);
           $('#modalnumingreso').html(result.numero_ingreso);

           var total=0;
          $.each(result.detalle,function(index,datos){
                      
                      
                        var subtotal=datos.cantidad*datos.precio_compra;
                            total = total+subtotal;                                                 

                         tabla.row.add( [  datos.articulo,
                                           datos.cantidad,
                                           datos.precio_compra,
                                           datos.serial,
                                           datos.placa,
                                           subtotal 
                                         ] ).draw();
                          
                               
            });
          
           $('#modaltotal').html('$'+total);
          $('#modal-show').modal('show');
         
         });

        
               
        }); //fin función btn-show


});
