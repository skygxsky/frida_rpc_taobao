Java.perform(function () {
    function test1() {
        // TCP false
        var obj = Java.use('mtopsdk.mtop.global.SwitchConfig');
        obj.isGlobalSpdySwitchOpen.implementation = function () {
            var res = this.isGlobalSpdySwitchOpen();
            // send("res==>" + res);
            return false;
        }
    }

    function test2() {
        // var obj = Java.use('tb.orb');
        // obj.a.overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean').implementation = function (a,b,c,d,e) {
        //     send("a==>"+a);
        //     send("b==>"+b);
        //     send("c==>"+d);
        //     send("d==>"+d);
        //     send("e==>"+e);
        //     var res = this.a(a,b,c,d,e);
        //     send("res==>" + res);
        //     return res;
        // }

        // var obj = Java.use('tb.ora');
        // obj.a.overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean').implementation = function (a,b,c,d,e) {
        //     send("a==>"+a);
        //     send("b==>"+b);
        //     send("c==>"+d);
        //     send("d==>"+d);
        //     send("e==>"+e);
        //     var res = this.a(a,b,c,d,e);
        //     send("res==>" + res);
        //     return res;
        // }
        var obj = Java.use('tb.orc');
        obj.a.overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean').implementation = function (a,b,c,d,e) {
            send("a==>"+a);
            send("b==>"+b);
            send("c==>"+d);
            send("d==>"+d);
            send("e==>"+e);
            var res = this.a(a,b,c,d,e);
            send("res==>" + res);
            return res;
        }
    }

    function test3() {
        var obj = Java.use('com.alibaba.wireless.security.open.middletier.IUnifiedSecurityComponent')
        obj.getSecurityFactors.implementation = function (a) {
            send("a==>" + a);
            var res = this.getSecurityFactors(a);
            send("res==>" + res);
            return res
        }
    }
    function test4() {
        // params
        var obj = Java.use('mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl');
        obj.buildParams.implementation = function (a) {
            send("4 a==>" + a);
            var res = this.buildParams(a);
            send("4 res==>" + res);
            return res
        }
    }

    test1()
    test2() //x-sign
    // test3()
    test4()
})
