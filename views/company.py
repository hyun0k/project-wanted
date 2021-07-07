from flask          import request, jsonify
from models.company import * 

from flask import current_app as app

@app.route("/company", methods=["GET"])
def search_company():
    try:
        keyword = request.args.get('name')
    
        is_exist_in_ko = db.session.query(CompanyKo.query.filter(CompanyKo.name.ilike(f'%{keyword}%')).exists()).scalar()
        is_exist_in_en = db.session.query(CompanyEn.query.filter(CompanyEn.name.ilike(f'%{keyword}%')).exists()).scalar()
        is_exist_in_ja = db.session.query(CompanyJa.query.filter(CompanyJa.name.ilike(f'%{keyword}%')).exists()).scalar()

        if is_exist_in_ko:
            companies = CompanyKo.query.filter(CompanyKo.name.ilike(f'%{keyword}%')).all()
        
        if is_exist_in_en:
            companies = CompanyEn.query.filter(CompanyEn.name.ilike(f'%{keyword}%')).all()
        
        if is_exist_in_ja:
            companies = CompanyJa.query.filter(CompanyJa.name.ilike(f'%{keyword}%')).all()

        result = []
        for company in companies:
            company_id = company.company_id
            
            company_ko = CompanyKo.query.filter_by(company_id=company_id).one()
            company_en = CompanyEn.query.filter_by(company_id=company_id).one()
            company_ja = CompanyJa.query.filter_by(company_id=company_id).one()
            
            company_tags = Tag.query.filter(Tag.tags_companies.any(company_id=company_id)).all()
            
            tag_list_ko = [
                {
                    'id'   : tag.id,
                    'name' : TagKo.query.filter_by(tag_id=tag.id).one().name
                } for tag in company_tags
            ]
 
            tag_list_en = [
                {
                    'id'   : tag.id,
                    'name' : TagEn.query.filter_by(tag_id=tag.id).one().name
                } for tag in company_tags
            ]
            
            tag_list_ja = [
                {
                    'id'   : tag.id,
                    'name' : TagJa.query.filter_by(tag_id=tag.id).one().name
                } for tag in company_tags
            ]

            result.append(
                {
                    'id' : company_id,
                    'company_name_ko' : company_ko.name if company_ko.name else None,
                    'company_name_en' : company_en.name if company_en.name else None,
                    'company_name_ja' : company_ja.name if company_ja.name else None,
                    'company_tag_ko'  : tag_list_ko,
                    'company_tag_en'  : tag_list_en,
                    'company_tag_ja'  : tag_list_ja
                }
            )

        return jsonify({"message" : result}), 201
    
    except KeyError:
        return jsonify({"message" : "KEY_ERROR"}), 400
    
