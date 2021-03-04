## Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin
 Interpreter dillər kodları sətir-sətir tərcümə edir.Yəni,hər bir kod sətri ardıcıllıqla yoxlanılır, tərcümə olunur və əgər kodun bir sətrində səhv aşkar olunarsa, digər sətrə keçmədən prosesi dayandırır.Python,JavaScript,Ruby bu dillərə misaldır.Həmçinin heç bir əlavə obyekt kod yaratmır və yaddaşı daha səmərəli istifadə edir.
***
## Interpreted və compiler dillər arasında olan fərqləri izah edin
##### | Interpreter |
- Proqramı sətir-sətir yoxlayır
- Obyekt kodu yaratmır,yaddaşı daha səmərəli istifadə 
- Kodun təhlili üçün az vaxt gedir
- İcra prosesi uzundur
##### | Compiler |
- Proqramı bütünlüklə tərcümə edir
- Obyekt kodu yaratdığı üçün daha çox yer istifadə olunur
- Kodun təhlili üçün çox vaxt gedir
- İcra prosesi qısadır


***
## Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin
* Mətn növü - STR | söz,cümlə,yazı və.s bu kimi məlumatları daxil etmək üçün istifadə olunur |
* Ədəd növləri - İNT,FLOAT | rəqəmləri,ədədləri daxil etmək üçün istifadə olunur |
* Sıra növləri - LİST,TUPLE,RANGE | birdən çox məlumatı birlikdə saxlamaq üçün istifadə olunur |
* Boolean növü - BOOL | yalnız 2 dəyər ala bilir : True/False |
* DİCT | Məlumatları yerləşdirmək üçün istifadə olunur ama diərlərindən fərqli cəhəti odurki bu zaman key"lerden istifade edirik. |
***

## Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?
Normalda metodlar olmasaydı,biz bir məsələni alqoritmlər quraraq uzun uzun kod sətirləri yazırıq.Python,nəinki python bütün dillərdə metodlar var və
dilləri yaradan proqramçılar uzun uzun kod sətirləri yazılmasın deyə eyni prosesi yerinə yetirən metodları yaradıblar. 
***
## local və global variable nədir izah edin
* Local deyisken - funksiya daxilinde teyin etdiyimiz deyiskenlere deyilir,bu deyiskenlere teyin olunan funksiya xaricinde istifade etmek mumkun olmur.
* Global deyisken - funksiya xaricinde teyin edilen deyiskenlere deyilir ve bu deyiskenlere istediyimiz yerde cagira bilirik
***
## Python type conversion haqqında izahat verin
Bir məlumat növünün digər məlumat növünə çevrilməsinə **Type Conversion** deyilir. 
### 2 növü var :
- Implicit Type Conversion 
- Explicit Type Conversion
* Implicit t.c - məsələn **int -> float** çevrilmə implicit type conversion hesab olunur.
* Explicit t.c - məsələn **int -> str** çevrilmə explicit type conversion hesab olunur. 

***
## init nədir?
Biz **init()** funksiyasından istifadə edərək obyekt xüsusiyyətlərinə dəyərlər təyin edə bilərik.İnit() ilə contact qurmaq üçünsə self parametrini əlavə edirik.
***
## self nədir?
**Self** -Pythonda class'i təmsil edən metodların ilk parametridir, buna gore class daxilindeki metodlari cagirmaq ucun self parametrinden istifade etmeliyik.
***
## *args,*kwargs nədir? nə zaman istifadə olunur?
Funksiyaya müəyyen sayda arqument əlavə etmək lazımdırsa istifadə edilir.
***
## Python module nədir?
Pythondakı modullar sadəcə .py uzantılı Python sənədləridir. Modulun adı faylın adı olacaqdır. Python modulu müəyyən edilmiş və həyata keçirilmiş bir sıra funksiyalar, siniflər və ya dəyişənlərə sahib ola bilər.
***
## Python package nədir?
Python package (PIP) - Python paketləri və ya modullar üçün paket meneceridir. Paket bir modul üçün lazım olan bütün sənədləri əhatə edir.
***
## pass nədir? Nə zaman istifadə olunur?
Bir növ keçid ifadəsidir.Heç bir əməliyyat yerinə yetirmədikdə pass istifade edirik ki,kodlar tercume olunarkən error verməsin. Həm də sonradan o hissəyə kod əlavə edə bilək deyə bir növ yer tutur kodlarımız üçün.
***
## List metodlarından 5 ədəd metodun izahatını yazın
- append () Siyahının sonuna bir element əlavə edir
- clear () Bütün elementləri siyahıdan çıxarır
- pop () Elementi göstərilən mövqedən sili
- count () Müəyyən olunmuş dəyərə malik elementlərin sayını qaytarır
- sort () Siyahını sıralayır
***
## List və dict hansı hallarda istifadə olunur?
LIST birdən çox maddəni bir dəyişəndə ​​saxlamaq üçün istifadə olunur. DICT isə məlumat dəyərlərini (key: value) saxlamaq üçün istifadə olunur. Bundan əlavə Dict sifariş edilmiş, dəyişdirilə bilən və təkrarlanmağa icazə verilməyən bir kolleksiyadır. Hər hansı məlumatları siyahıya almaq istədiyimizdə LİST, onların (və ya başqa halda) dəyərlər saxlamasını istədiyimizdə DİCT istifadə edə bilərik.
***
## Dict metodlarından 5 ədəd metodun izahatını yazın
- clear () Dict daxilindəki bütün elementləri silir
- copy () Dict -in surətini qaytarır
- get () Göstərilən açarın (key) dəyərini qaytarır
- pop () Göstərilən açar ilə elementi (value) silir
- values () Dict -dəki bütün dəyərlərin siyahısını qaytarır