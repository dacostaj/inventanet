$(document).ready(function(){

	var total=0;
	var contador=0;
	var subtotal=[];

//	$('#pidarticulo').change(mostrarValores);

	function mostrarValores(){

		var verificacion = $('#pidarticulo').val();

	if(verificacion == 'ninguno'){
		$('#idinputpcompra').val('');
		$('#idinputcantidad').val('');
		$('#idinputserial').val('');
		$('#idinputcantidad').prop('disabled', false);
	}else{

	var	datosarticulo = document.getElementById('pidarticulo').value.split('_');

	var tipo = datosarticulo[1].toLowerCase();

	if(tipo == 'devolutivo'){
		$('#idinputcantidad').prop('disabled', true);
		$('#idinputcantidad').val(1);
	}
	else{
		$('#idinputcantidad').prop('disabled', false);
	}

	}// fin if/else principal
	
	}// fin de la función mostrar


	
	$('#guardar').attr("disabled", true);//deshabilitar boton el boton guardar al incio
	$('#alertaingreso').hide(); //ocultamos el div alerta

	$('#btn_add').click(agregar); //escucha el evento click del boton agregar

	
	function agregar(){
		//var	datosarticulo = document.getElementById('pidarticulo').value.split('_');
		//var idarticulo =	datosarticulo[0];
		var idarticulo = document.getElementById('pidarticulo').value;	
		var articulo   =	$('#pidarticulo option:selected').text();
		var cantidad   =	$('#idinputcantidad').val();	
		var pcompra    =	$('#idinputpcompra').val();	
		var serial     =	$('#idinputserial').val();

		if (idarticulo!="" && cantidad!="" && pcompra!="" && serial!="" && cantidad>0) {

			subtotal[contador] = (cantidad*pcompra);
			subtotalvar =  subtotal[contador];
			total = total + subtotal[contador];

			var table = $('#idtabladetalle').DataTable();
			var fila = table
			    .row.add( [ '<button type="button" id="'+contador+'" class="btn btn-detalle btn-danger"><i class="fa fa-close"></i></button>',
			    		    '<input type="hidden" name="idarticulo[]" value="'+idarticulo+'">'+articulo+'</input>',
			    		    '<input type="hidden" name="cantidad[]" readonly="readonly" value="'+cantidad+'">'+cantidad+'</input>',
			    		    '<input type="hidden" name="pcompra[]" readonly="readonly" value="'+pcompra+'">'+pcompra+'</input>',
			    		    '<input type="hidden" name="serial[]" readonly="readonly" value="'+serial+'">'+serial+'</input>',
			    		     subtotalvar
			    		    ] )
			    .draw();
			
			contador++;
			limpiar();
			$('#total').html('$ '+total);
			evaluar();
			
		    		
		} else{

			  $('#alertaingreso').show();
			  $("#alertaingreso").fadeOut(4000);
		}

		

	}//fin del evento click del boton agregar

	
	$('#idtabladetalle').dataTable().on( 'click', 'td button', function () {
	  	var row = $(this).parents('tr');
	  	var id = $(this).attr('id');
	  	row.fadeOut();
	  	total = total - subtotal[id];
		$('#total').html('$'+total);

    }); //fin del metodo eliminar 
	    
	    
	

	function limpiar() {

			//$('#idinputcantidad').val('');	
			//$('#idinputpcompra').val('');	
			//$('#idinputpventa').val('');	

		}//fin del metodo limpiar

	function evaluar(){

			if (total > 0) {

				$('#guardar').attr("disabled", false);
			} 

				else {
						$('#guardar').attr("disabled", true);
				}


		} //fin del metodo evaluar



});


