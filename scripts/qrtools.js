var init = function() {
	
	var spinner = function(id){
		$(id).html('<div class="spinner"></div>')
	}

	var loadError = function(id, errorThrown, timeout){
		timeout=timeout||2000;
		errorThrown=errorThrown||"";
		$(id).html('<div class="ui-widget errorBox"><div class="ui-state-error ui-corner-all" style="padding: 0 .7em;"><p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span><strong>Something went wrong!</strong></p><p>'+errorThrown+'<p/></div></div>').children().fadeOut(timeout, function(){$(this).parent().html('')});
	}

	var validateError = function(id, errorThrown, timeout){
		timeout=timeout||2000;
		errorThrown=errorThrown||"Something went wrong!";
		$(id).html('<div class="ui-widget errorBox"><div class="ui-state-highlight ui-corner-all" style="margin-top: 20px; padding: 0 .7em;"><p><span class="ui-icon ui-icon-info" style="float: left; margin-right: .3em;"></span><strong>'+errorThrown+'</strong></p></div></div>').children().fadeOut(timeout, function(){$(this).parent().html('')});
	}
	
	$("#qrSubmit").button().click(function() {
		//$('#dbug').append('submitting<br/>');
		//$('#dbug').append('type: '+$("#qrInput").attr('name')+'<br/>');
		
		if($("#qrInput").val()==''){
			//$('#dbug').append('field empty<br/>');
			validateError('#result', 'Empty field!', 2000)
			return false;
		}
		
		$.ajax({
			url:"/qra?"+$("#qrInput").attr('name')+"="+$("#qrInput").val(),
			type:'GET',
			beforeSend: function(){
				spinner('#result')
				//$('#dbug').append('spinning<br/>');
			},
			success: function(html){
				$('#result').html(html);
				//$('#dbug').append('success!<br/><br/>');
			},
			error: function( jqXHR,  textStatus,  errorThrown){
				loadError('#result', jqXHR.status + ' - ' + errorThrown, 5000)
				//$('#dbug').append('error!<br/>'+textStatus+' '+jqXHR.status+'<br/>'+errorThrown+'<br/><br/>');
			},
		});
	});
	
	$('#qrInput').keypress(function (e) {
		if (e.which == 13) {
			$("#qrSubmit").click();
			return false;
		}
	});
	
	$("#qrTypeSelect").button({
		text: false,
		icons: {
			primary: "ui-icon-triangle-1-s"
		}
	})
	$("#qrTypeSelect, #qrType").click(function() {
		var menu = $("#qrTypeSelectList").show().position({
			my: "left top",
			at: "left bottom",
			of: this
		});
		$(document).one("click", function() {
			menu.hide();
		});
		return false;
	});
	
	$("#showhelp").button({
		text: false,
		icons: {
			primary: "ui-icon-help"
		}
	}).click(function() {
		if ($('#hidden').is( ":visible" )){
			$('#hidden').slideUp( 500 );
		} 
		else {
			$('#hidden').slideDown( 500 );
	}
		return false;
	});
	
	$("#qrForm").buttonset()
	$("#qrTypeSelectList").hide().menu({
		select: function(event, ui) {
			$("#qrType").button('option', 'label', ui.item.text());
			$("#qrInput").attr("placeholder" , ui.item.children().attr('placeholder')).attr("name" , ui.item.children().attr('name'));
		}
	});
}

