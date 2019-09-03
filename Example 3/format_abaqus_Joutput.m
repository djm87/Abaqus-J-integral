fname=fullfile(pwd,'odb','J-Indenter_Quarter_homo.dat')

%positions (corner nodes) 
positions=[2.781500,2.682161,2.582822,2.483482,2.384143,2.284804,2.185465,2.086125,1.986786,1.887447,1.788107,1.688768,1.589429,1.490089,1.390750,1.291411,1.192071,1.092732,0.993393,0.894054,0.794714,0.695375,0.596036,0.496696,0.397357,0.298018,0.198679,0.099339,0.000000]


%offset from step time to J
offset=15
%offset between slices
offsetSlice=5
%number of slices
nSlices=57

%number of contour levels
nContours=20;

JAll=zeros(nSlices,20)
c=textread(fname,'%s','delimiter','\n');

for i=1:length(c)
    line=c{i};
    if contains(line,'STEP TIME COMPLETED')
        lineId=i;
        tmp=strsplit(line);
        time=str2double(tmp{4})
        lineId=i+offset
        for j =1:nSlices
            lineId=i+offset+offsetSlice*(j-1)
            contourCnt=1;
            for k=0:offsetSlice-2
                line=c{lineId+k}
                tmp=strsplit(line);  
                for l=1:length(tmp)
                    val=str2double(tmp{l})
                    if and(~isnan(val),~isempty(val))
                       JAll(j,contourCnt)=val;
                       contourCnt=contourCnt+1;  
                    end
                end
            end
        end
         JAll=flipud(JAll)
        %save frame to file
        fnameOut=sprintf('Js-Abaqus-at-time-%.3f',time)
        fnameOut=[strrep(fnameOut,'.','p'),'.txt']
        fileID = fopen(fnameOut,'w');
        cnt=0
        fprintf(fileID,'nan');
        for i=1:length(positions)
            fprintf(fileID,',%f',positions(i));
        end
        for i=1:nContours
            fprintf(fileID,'\n%d',i);
            for j=1:2:nSlices
                fprintf(fileID,',%16.10f',JAll(j,i));
            end
        end
        fclose(fileID);
        
        
    end
        
end